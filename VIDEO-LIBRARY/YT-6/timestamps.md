# YT-6 — System Design of Youtube | Mock Interview 5+ years of Experience | HLD | Code Decode

**Video:** https://www.youtube.com/watch?v=35lPXRd00-8 · **32 distinct interview questions** · **86 curated timestamp sections**.

[Pure video chronological timeline](timeline.md) · [Unedited full linked transcript](transcript.md) · [Coverage audit](coverage-audit.md)

⭐ means this interview question already exists elsewhere in the library, so its permanent ID is reused.

## Find a question

| Watch | Question |
|---|---|
| [0:58](https://www.youtube.com/watch?v=35lPXRd00-8&t=58s) | [IA-42 — How would you define functional requirements for a YouTube-like service?](#ia-42) |
| [4:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=279s) | [IA-43 — Which nonfunctional requirements matter for a video platform?](#ia-43) |
| [5:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=356s) | [IA-44 — How would you estimate daily active users and video viewing volume?](#ia-44) |
| [7:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=465s) | [IA-45 — How do you estimate daily video storage requirements?](#ia-45) |
| [9:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=558s) | [IA-46 — How would you estimate CDN bandwidth and delivery costs?](#ia-46) |
| [11:51](https://www.youtube.com/watch?v=35lPXRd00-8&t=711s) | [IA-47 — How does autoscaling help a video streaming service?](#ia-47) |
| [13:26](https://www.youtube.com/watch?v=35lPXRd00-8&t=806s) | [IA-48 — Why are replication and fault tolerance important for video data?](#ia-48) |
| [14:17](https://www.youtube.com/watch?v=35lPXRd00-8&t=857s) | [IA-49 — How would you make large video uploads resumable?](#ia-49) |
| [15:46](https://www.youtube.com/watch?v=35lPXRd00-8&t=946s) | [IA-50 — Why does video transcoding produce multiple resolutions and bitrates?](#ia-50) |
| [16:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=1016s) | [IA-51 — How does adaptive bitrate streaming avoid long playback delays?](#ia-51) |
| [18:14](https://www.youtube.com/watch?v=35lPXRd00-8&t=1094s) | [IA-52 — How would you detect and retry missing video upload chunks?](#ia-52) |
| [21:13](https://www.youtube.com/watch?v=35lPXRd00-8&t=1273s) | [IA-53 — What services participate in an end-to-end video upload pipeline?](#ia-53) |
| [27:49](https://www.youtube.com/watch?v=35lPXRd00-8&t=1669s) | [ID-5 — How would you choose SQL or NoSQL for video metadata?](#id-5) |
| [29:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=1785s) | [IA-54 — Why deliver processed videos through a CDN?](#ia-54) |
| [31:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=1878s) | [IA-55 — How would you manage video upload status and completion notifications?](#ia-55) |
| [34:06](https://www.youtube.com/watch?v=35lPXRd00-8&t=2046s) | [ID-2 — Explain table partitioning versus database sharding.](#id-2) ⭐ |
| [36:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=2175s) | [ID-6 — What is the difference between data partitioning and replication?](#id-6) |
| [37:58](https://www.youtube.com/watch?v=35lPXRd00-8&t=2278s) | [IA-56 — How can a video ID route a request to the correct metadata shard?](#ia-56) |
| [39:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=2363s) | [IA-57 — How would you design the watch-video request path?](#ia-57) |
| [40:19](https://www.youtube.com/watch?v=35lPXRd00-8&t=2419s) | [IA-58 — What is MPEG-DASH or adaptive streaming over HTTP?](#ia-58) |
| [43:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=2636s) | [IA-59 — How does global upload latency differ from playback latency?](#ia-59) |
| [46:55](https://www.youtube.com/watch?v=35lPXRd00-8&t=2815s) | [IA-60 — How would you collect video engagement signals for recommendations?](#ia-60) |
| [48:32](https://www.youtube.com/watch?v=35lPXRd00-8&t=2912s) | [IA-61 — How do you keep popular videos hot in a CDN cache?](#ia-61) |
| [51:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=3078s) | [IA-62 — How would you build creator analytics for views and watch time?](#ia-62) |
| [55:05](https://www.youtube.com/watch?v=35lPXRd00-8&t=3305s) | [IA-63 — How do likes, comments, and click-through rate influence recommendations?](#ia-63) |
| [56:54](https://www.youtube.com/watch?v=35lPXRd00-8&t=3414s) | [IA-64 — How would you store video thumbnails and generate previews?](#ia-64) |
| [1:00:02](https://www.youtube.com/watch?v=35lPXRd00-8&t=3602s) | [IA-65 — What are codecs and why do they matter to video platforms?](#ia-65) |
| [1:02:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=3735s) | [IA-66 — How do bitrate, frame rate, and resolution affect video storage?](#ia-66) |
| [1:06:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=3975s) | [IA-67 — How do background workers process video transcoding jobs reliably?](#ia-67) |
| [1:09:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=4163s) | [IA-68 — What components make up a video transcoding architecture?](#ia-68) |
| [1:12:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=4347s) | [IA-69 — How do job queues and priorities control video transcoding work?](#ia-69) |
| [1:17:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=4659s) | [IA-70 — How can presigned URLs safely authorize media uploads or downloads?](#ia-70) |

## Non-question source context — intros, promotions and closing

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.1 | [0:00](https://www.youtube.com/watch?v=35lPXRd00-8&t=0s) | 🟡 INTRO | Interview introduction and candidate background |
| YT-6.84 | [1:20:03](https://www.youtube.com/watch?v=35lPXRd00-8&t=4803s) | 🔴 NO NEED | Interview thank-you and closing |
| YT-6.85 | [1:21:14](https://www.youtube.com/watch?v=35lPXRd00-8&t=4874s) | 🔴 NO NEED | Interview thank-you and closing |
| YT-6.86 | [1:21:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=4905s) | 🔴 NO NEED | End of interview or closing remarks |

<a id="ia-42"></a>

## IA-42 — How would you define functional requirements for a YouTube-like service?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.2 | [0:58](https://www.youtube.com/watch?v=35lPXRd00-8&t=58s) | 🟢 USEFUL | How would you define functional requirements for a YouTube-like service? |
| YT-6.3 | [2:12](https://www.youtube.com/watch?v=35lPXRd00-8&t=132s) | 🟢 USEFUL | Follow-up: How would you define functional requirements for a YouTube-like service? |
| YT-6.4 | [3:24](https://www.youtube.com/watch?v=35lPXRd00-8&t=204s) | 🟢 USEFUL | Follow-up: How would you define functional requirements for a YouTube-like service? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:11](https://www.youtube.com/watch?v=35lPXRd00-8&t=71s) uh this is the place where you can have your diagrams created this is the plus sign you can draw anything any shape that you want Circle rectangle everything is here these are the things<br>[1:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=83s) that is common ones also you can have any Cloud items also say suppose uh you have cloud provider icons here so if you want to use a your database anything kubernetes anything that you want you | I'd start with video upload, playback, search, and basic creator analytics. Then I'd clarify comments, likes, subscriptions, recommendations, and supported devices. For example, letting users watch videos before implementing recommendations helps prioritize the core product. The requirements define what the system must do before choosing databases. |

<a id="ia-43"></a>

## IA-43 — Which nonfunctional requirements matter for a video platform?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.5 | [4:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=279s) | 🟢 USEFUL | Which nonfunctional requirements matter for a video platform? |
| YT-6.6 | [5:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=345s) | 🟢 USEFUL | Follow-up: Which nonfunctional requirements matter for a video platform? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [5:03](https://www.youtube.com/watch?v=35lPXRd00-8&t=303s) we want to ensure that whenever some note goes down we would want we want users to be able to a access the resources available online so if it's a multi microservice kind of an<br>[5:13](https://www.youtube.com/watch?v=35lPXRd00-8&t=313s) architecture if one note goes down we should be able to adhere to uh uh you know give the data back to the users as such overall speaking of consistency I think we can we can live with eventual | Availability, scalability, durability, latency, cost, and consistency are central for video streaming. For example, viewers want smooth playback during a popular live event, while comment counts might tolerate slight delay. I specify realistic targets for each feature rather than claiming the entire system needs identical consistency guarantees. |

<a id="ia-44"></a>

## IA-44 — How would you estimate daily active users and video viewing volume?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.7 | [5:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=356s) | 🟢 USEFUL | How would you estimate daily active users and video viewing volume? |
| YT-6.8 | [7:10](https://www.youtube.com/watch?v=35lPXRd00-8&t=430s) | 🟢 USEFUL | Follow-up: How would you estimate daily active users and video viewing volume? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [6:10](https://www.youtube.com/watch?v=35lPXRd00-8&t=370s) this number and make the estimations as per your requirement but this is something which is actually happening now day today in the real world with YouTube MH so actually you can make it<br>[6:22](https://www.youtube.com/watch?v=35lPXRd00-8&t=382s) yeah that's okay 5 billion users per day is a bit that too much but I think we can I think it's about 5 ion from what I remember the last time uh it's number of videos | I separate users, views, uploads, and bytes because they measure different things. For example, five million users watching five videos each gives 25 million daily views, not 25 million users. I'd multiply each activity by an assumed average size and call out those assumptions. Clear units prevent incorrect capacity estimates. |

<a id="ia-45"></a>

## IA-45 — How do you estimate daily video storage requirements?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.9 | [7:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=465s) | 🟢 USEFUL | How do you estimate daily video storage requirements? |
| YT-6.10 | [9:04](https://www.youtube.com/watch?v=35lPXRd00-8&t=544s) | 🟢 USEFUL | Follow-up: How do you estimate daily video storage requirements? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [8:00](https://www.youtube.com/watch?v=35lPXRd00-8&t=480s) 15 to 20 minutes of video size per average I would say and a 15 minute long video if you're dealing with let's say 1080ps uh of pure HD content then it it basically implies somewhere on about 120<br>[8:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=495s) FPS and uh one frame could be roughly around about um I guess uh not more than 1 MB or 2 MBS right okay so we can we're dealing with so roughly I'm assuming that this video size is supposedly 300 | I calculate daily upload count times average uploaded video size, then account for transcoded renditions and replication. For example, 500,000 uploads of 300 MB each represent about 150 TB of original video data per day before extra copies. Storage grows quickly, so I show assumptions separately from observed platform statistics. |

<a id="ia-46"></a>

## IA-46 — How would you estimate CDN bandwidth and delivery costs?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.11 | [9:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=558s) | 🟢 USEFUL | How would you estimate CDN bandwidth and delivery costs? |
| YT-6.12 | [10:32](https://www.youtube.com/watch?v=35lPXRd00-8&t=632s) | 🟢 USEFUL | Follow-up: How would you estimate CDN bandwidth and delivery costs? |
| YT-6.13 | [11:37](https://www.youtube.com/watch?v=35lPXRd00-8&t=697s) | 🟢 USEFUL | Follow-up: How would you estimate CDN bandwidth and delivery costs? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [9:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=579s) so I think we can live with um Amazon CDN I would say which is a cloud front CDN and if I assume that 100% of the traffics is sered from let's say the us because that's a headquarter of the<br>[9:52](https://www.youtube.com/watch?v=35lPXRd00-8&t=592s) video the average cost per GB average cost per GB is nearly about about I would say .5 per GB in that sense so we can I think it's kind of like side railing a little bit to the cost part of it but | I estimate daily video bytes delivered from average video size times watched videos, then multiply by the relevant bandwidth rate. For example, millions of 300 MB streams add up to petabytes of egress. Actual cost depends on regions, caching, video quality, and contracts. I would not present one guessed CDN price as a universal number. |

<a id="ia-47"></a>

## IA-47 — How does autoscaling help a video streaming service?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.14 | [11:51](https://www.youtube.com/watch?v=35lPXRd00-8&t=711s) | 🟢 USEFUL | How does autoscaling help a video streaming service? |
| YT-6.15 | [12:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=776s) | 🟢 USEFUL | Follow-up: How does autoscaling help a video streaming service? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [12:14](https://www.youtube.com/watch?v=35lPXRd00-8&t=734s) say um the daily active users from 5 million can go to let's say maybe 10 million okay consider just like doubling the numbers right yeah no problem so in that case we will have to account for<br>[12:28](https://www.youtube.com/watch?v=35lPXRd00-8&t=748s) the fact that we're looking at a daily storage of 300 terabytes of data even if I go extremely ahead of it or and let's say I'll do a 3X sort of a uh you know scale I would still be | Autoscaling adds capacity when CPU, traffic, or another useful metric rises and removes it when demand falls. For example, a new trailer can increase the number of API pods serving metadata requests. Scaling the API does not automatically scale storage or transcoding; each bottleneck needs its own strategy. |

<a id="ia-48"></a>

## IA-48 — Why are replication and fault tolerance important for video data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.16 | [13:26](https://www.youtube.com/watch?v=35lPXRd00-8&t=806s) | 🟢 USEFUL | Why are replication and fault tolerance important for video data? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [13:48](https://www.youtube.com/watch?v=35lPXRd00-8&t=828s) would be roughly around about uh 1.5 petabytes of data right okay so 1.5 FES of data over here okay I think this is a good enough scale for us to maintain in terms of YouTube overall I<br>[14:03](https://www.youtube.com/watch?v=35lPXRd00-8&t=843s) would say perfect also uh how about uh the fall tolerance in error handlings because there's a lot of scope of Errors happening in upload and uh viewing right right so uh basically when it comes to | A video platform must survive machine or zone failures without losing uploaded content. For example, storing durable object copies across failure domains can protect video segments. Replication helps availability and durability, but it also increases cost. I distinguish replica count from the number of active application pods. |

<a id="ia-49"></a>

## IA-49 — How would you make large video uploads resumable?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.17 | [14:17](https://www.youtube.com/watch?v=35lPXRd00-8&t=857s) | 🟢 USEFUL | How would you make large video uploads resumable? |
| YT-6.18 | [15:22](https://www.youtube.com/watch?v=35lPXRd00-8&t=922s) | 🟢 USEFUL | Follow-up: How would you make large video uploads resumable? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:29](https://www.youtube.com/watch?v=35lPXRd00-8&t=869s) trying to upload a video and all of a sudden there was a network issue so I was not able to upload the video perfectly so we we can add some checkpoints in terms of 300 like 300 MBS<br>[14:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=879s) of data is not that much actually so uploading 300 MBS on on a cloud storage would imply that I'm let's say if it if there's a failure in this upload process I can just ask the person to upload the | I'd split an upload into numbered chunks, persist completed-chunk metadata, and retry only missing or invalid chunks. For example, if part seven fails, the client does not have to restart a 2 GB upload. An upload session ID, checksums, and completion verification help prevent corruption or duplicate parts. |

<a id="ia-50"></a>

## IA-50 — Why does video transcoding produce multiple resolutions and bitrates?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.19 | [15:46](https://www.youtube.com/watch?v=35lPXRd00-8&t=946s) | 🟢 USEFUL | Why does video transcoding produce multiple resolutions and bitrates? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:10](https://www.youtube.com/watch?v=35lPXRd00-8&t=970s) maybe a 1080p video not every device or every network will be able to stream that so because of codc value being limited down to 1080p 720p 480p 360p and so on and so forth we can have a<br>[16:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=983s) paralyzation happening at the back end which is taking one single video of that 300 MBS and then storing them on multiple bit rates upon upon in the codec value onto some sort of a database | The same video needs versions suitable for different devices and networks. For example, a phone on slow mobile data may play 480p while a TV on Wi-Fi plays 1080p. An asynchronous transcoding pipeline produces these renditions before they are served. This lets the player adapt quality without reprocessing the original video. |

<a id="ia-51"></a>

## IA-51 — How does adaptive bitrate streaming avoid long playback delays?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.20 | [16:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=1016s) | 🟢 USEFUL | How does adaptive bitrate streaming avoid long playback delays? |
| YT-6.21 | [18:01](https://www.youtube.com/watch?v=35lPXRd00-8&t=1081s) | 🟢 USEFUL | Follow-up: How does adaptive bitrate streaming avoid long playback delays? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [17:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=1036s) batches such that I would know that this for from 1 minute to 10 minute there's a certain PCH which has been loaded and once that part has been completed or about to be completed the second part<br>[17:25](https://www.youtube.com/watch?v=35lPXRd00-8&t=1045s) starts loading automatically for a more seamless experience that way I can also uh encounter for the part that in case my network latency goes very very high which means my network bit rate has | The client downloads short video segments and can switch among available bitrates based on buffer and network conditions. For example, if bandwidth drops, the next segment can use a lower-quality rendition. HLS and MPEG-DASH are common techniques. The viewer starts playback without waiting for the entire video file. |

<a id="ia-52"></a>

## IA-52 — How would you detect and retry missing video upload chunks?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.22 | [18:14](https://www.youtube.com/watch?v=35lPXRd00-8&t=1094s) | 🟢 USEFUL | How would you detect and retry missing video upload chunks? |
| YT-6.23 | [19:20](https://www.youtube.com/watch?v=35lPXRd00-8&t=1160s) | 🟢 USEFUL | Follow-up: How would you detect and retry missing video upload chunks? |
| YT-6.24 | [20:26](https://www.youtube.com/watch?v=35lPXRd00-8&t=1226s) | 🟢 USEFUL | Follow-up: How would you detect and retry missing video upload chunks? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [18:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=1107s) it's because what happens is if multiple times a particular chunk is uploaded you will see the same chunk twice or else what happens is if one of the Chunk in between is left to be uploaded how would<br>[18:37](https://www.youtube.com/watch?v=35lPXRd00-8&t=1117s) you handle such situations right so in that case uh we are not we can we can basically have check sums Associated for every chunk which passes by right like it's a | I track chunk numbers, checksums, and upload completion status. For example, if chunks 1 through 9 arrived except 4, the system requests or retries chunk 4 before finalizing. A checksum proves data integrity, while a manifest checks which parts are present. I do not mark a video ready until the expected chunks verify. |

<a id="ia-53"></a>

## IA-53 — What services participate in an end-to-end video upload pipeline?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.25 | [21:13](https://www.youtube.com/watch?v=35lPXRd00-8&t=1273s) | 🟢 USEFUL | What services participate in an end-to-end video upload pipeline? |
| YT-6.26 | [22:25](https://www.youtube.com/watch?v=35lPXRd00-8&t=1345s) | 🟢 USEFUL | Follow-up: What services participate in an end-to-end video upload pipeline? |
| YT-6.27 | [23:31](https://www.youtube.com/watch?v=35lPXRd00-8&t=1411s) | 🟢 USEFUL | Follow-up: What services participate in an end-to-end video upload pipeline? |
| YT-6.28 | [24:38](https://www.youtube.com/watch?v=35lPXRd00-8&t=1478s) | 🟢 USEFUL | Follow-up: What services participate in an end-to-end video upload pipeline? |
| YT-6.29 | [25:43](https://www.youtube.com/watch?v=35lPXRd00-8&t=1543s) | 🟢 USEFUL | Follow-up: What services participate in an end-to-end video upload pipeline? |
| YT-6.30 | [26:55](https://www.youtube.com/watch?v=35lPXRd00-8&t=1615s) | 🟢 USEFUL | Follow-up: What services participate in an end-to-end video upload pipeline? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [21:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=1299s) worries I got that so let's say I want to talk about the upload flow so there are multiple users who are trying to upload this video it could be coming from a like from a TV maybe or a laptop<br>[21:50](https://www.youtube.com/watch?v=35lPXRd00-8&t=1310s) maybe or whatever different devices which Ur over here so I'll need some sort of a load balancer first of all to be able to deal with uh this this thing right like where exactly to which | An upload API authenticates the creator and accepts metadata, temporary storage receives bytes, a completion event triggers transcoding, and processed renditions go to durable object storage and CDN distribution. For example, the creator sees a processing state while background workers generate 720p and 1080p versions. Each stage needs retry and status tracking. |

<a id="id-5"></a>

## ID-5 — How would you choose SQL or NoSQL for video metadata?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.31 | [27:49](https://www.youtube.com/watch?v=35lPXRd00-8&t=1669s) | 🟢 USEFUL | How would you choose SQL or NoSQL for video metadata? |
| YT-6.32 | [29:02](https://www.youtube.com/watch?v=35lPXRd00-8&t=1742s) | 🟢 USEFUL | Follow-up: How would you choose SQL or NoSQL for video metadata? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [28:05](https://www.youtube.com/watch?v=35lPXRd00-8&t=1685s) very wide column sort of a thing it could be description it could be uh it could be like uh what what particular channel is is is the video coming from it could be how what users are we uh<br>[28:20](https://www.youtube.com/watch?v=35lPXRd00-8&t=1700s) trying to Target in that sense it could be like all the sort of backend things which which people generally put up on YouTube videos I'm not too sure because I've never actually upad a YouTube video | Video metadata commonly has stable fields such as ID, owner, title, and status, which can fit a relational database. Flexible attributes or enormous access patterns may justify a document store. For example, comments and view events may be stored separately from core video records. I choose based on queries and consistency, not simply because a video is a large file. |

<a id="ia-54"></a>

## IA-54 — Why deliver processed videos through a CDN?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.33 | [29:45](https://www.youtube.com/watch?v=35lPXRd00-8&t=1785s) | 🟢 USEFUL | Why deliver processed videos through a CDN? |
| YT-6.34 | [30:55](https://www.youtube.com/watch?v=35lPXRd00-8&t=1855s) | 🟢 USEFUL | Follow-up: Why deliver processed videos through a CDN? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [30:00](https://www.youtube.com/watch?v=35lPXRd00-8&t=1800s) content delivery Network right so it it will be having its own cach it's like a different system altoe just like handing it down uh to the third party service to be able to deliver it on on the go so<br>[30:10](https://www.youtube.com/watch?v=35lPXRd00-8&t=1810s) yes it will be having its own internal caches and own internal data basis and things like that from which will'll be fing the uh the things so yeah correct okay okay and here the CDN are also from | A CDN caches popular video segments near viewers so the origin storage does not serve every request. For example, viewers in India can fetch a popular trailer from a nearby edge rather than repeatedly accessing one remote object bucket. This cuts latency and origin load. Cache-miss and invalidation behavior still matter. |

<a id="ia-55"></a>

## IA-55 — How would you manage video upload status and completion notifications?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.35 | [31:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=1878s) | 🟢 USEFUL | How would you manage video upload status and completion notifications? |
| YT-6.36 | [32:25](https://www.youtube.com/watch?v=35lPXRd00-8&t=1945s) | 🟢 USEFUL | Follow-up: How would you manage video upload status and completion notifications? |
| YT-6.37 | [33:40](https://www.youtube.com/watch?v=35lPXRd00-8&t=2020s) | 🟢 USEFUL | Follow-up: How would you manage video upload status and completion notifications? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:41](https://www.youtube.com/watch?v=35lPXRd00-8&t=1901s) metadata part which I think we stressed upon earlier as well so while the file is being uploaded to the original storage at that point of time the client will send a parallel request to the API<br>[31:52](https://www.youtube.com/watch?v=35lPXRd00-8&t=1912s) server to process the metadata because again we don't want it to be like a synchronous flow it will be completely asynchronous flow so we can say that once the request has been sent in | I keep an explicit upload state such as RECEIVING, PROCESSING, READY, or FAILED, and update it as chunks verify and transcoding finishes. For example, a creator should not get a playable link before a usable rendition exists. Events and idempotent handlers help progress safely through retries. |

<a id="id-2"></a>

## ID-2 — Explain table partitioning versus database sharding. ⭐

⭐ **Repeated interview question:** reused **ID-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.38 | [34:06](https://www.youtube.com/watch?v=35lPXRd00-8&t=2046s) | 🟢 USEFUL | How does partitioning or sharding scale a video metadata database? |
| YT-6.39 | [35:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=2116s) | 🟢 USEFUL | Follow-up: How does partitioning or sharding scale a video metadata database? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:29](https://www.youtube.com/watch?v=35lPXRd00-8&t=2069s) horizontal scaling in that sense but having said that if we do want to do that if we want to scale it horizontally by adding a couple of more pods to it we can we can do that with basic uh uh<br>[34:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=2079s) scaling or you know like scaling practices by spawning new record new uh New Ports for it and then start storing sequentially in terms of the uh uh you know SQL servers maybe or or by spawning | Partitioning groups rows by a useful key, while sharding spreads data across database nodes. For example, video metadata can be sharded by a stable video ID when one database can no longer handle write volume. The routing key must spread load without breaking common queries. Replication serves a different purpose from sharding. |

<a id="id-6"></a>

## ID-6 — What is the difference between data partitioning and replication?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.40 | [36:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=2175s) | 🟢 USEFUL | What is the difference between data partitioning and replication? |
| YT-6.41 | [37:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=2247s) | 🟢 USEFUL | Follow-up: What is the difference between data partitioning and replication? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [36:33](https://www.youtube.com/watch?v=35lPXRd00-8&t=2193s) could be having um what else I think that's about it that's that's we can live with this right right so as in when the field start getting populated into this uh uh database let's say I have<br>[36:47](https://www.youtube.com/watch?v=35lPXRd00-8&t=2207s) filled probably 1 million rows in this format so I would just want to exact same replica of this database once again okay sounds good so that that's why the Partition by row would imply that I have | Partitioning divides the data set, and replication keeps additional copies of the same data. For example, two shards may store different video ID ranges, while each shard has multiple replicas for resilience. Partitioning addresses data volume or load; replication protects availability and reads. They are often used together. |

<a id="ia-56"></a>

## IA-56 — How can a video ID route a request to the correct metadata shard?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.42 | [37:58](https://www.youtube.com/watch?v=35lPXRd00-8&t=2278s) | 🟢 USEFUL | How can a video ID route a request to the correct metadata shard? |
| YT-6.43 | [39:09](https://www.youtube.com/watch?v=35lPXRd00-8&t=2349s) | 🟢 USEFUL | Follow-up: How can a video ID route a request to the correct metadata shard? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [38:25](https://www.youtube.com/watch?v=35lPXRd00-8&t=2305s) okay uh just a second take your time yeah so a video ID followed by the database information instance number for works yeah basically a pointer to a pointer to database instance yeah yeah that's what<br>[38:43](https://www.youtube.com/watch?v=35lPXRd00-8&t=2323s) perfect perfect so perfect with the help of this we can identify the database and then fetch the information name whatever requires is okay so I I would rather call it as a | A routing layer applies a consistent mapping from video ID to a shard or partition. For example, a hashed ID can identify which database stores a video's metadata. The mapping must support growth and shard movement without losing records. Clients should not need to know the physical database location. |

<a id="ia-57"></a>

## IA-57 — How would you design the watch-video request path?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.44 | [39:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=2363s) | 🟢 USEFUL | How would you design the watch-video request path? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [39:43](https://www.youtube.com/watch?v=35lPXRd00-8&t=2383s) continuously receives the video streams from remote sources of videos so that's why it's like a streaming flow and not not rather a watching or a simple downloading flow over there now um when<br>[39:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=2396s) we watch stream in videos my client loads a little bit of data at a time so I can watch videos immediately and continuously so before we discuss too much into the video streaming flow let's | The client requests video metadata and a playback manifest, then retrieves video segments through a CDN. For example, starting a 45-minute video should fetch its first segments, not the full file. Authentication and playback authorization are checked as needed. Keeping metadata queries separate from segment delivery prevents API servers from carrying huge streams. |

<a id="ia-58"></a>

## IA-58 — What is MPEG-DASH or adaptive streaming over HTTP?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.45 | [40:19](https://www.youtube.com/watch?v=35lPXRd00-8&t=2419s) | 🟢 USEFUL | What is MPEG-DASH or adaptive streaming over HTTP? |
| YT-6.46 | [41:33](https://www.youtube.com/watch?v=35lPXRd00-8&t=2493s) | 🟢 USEFUL | Follow-up: What is MPEG-DASH or adaptive streaming over HTTP? |
| YT-6.47 | [42:41](https://www.youtube.com/watch?v=35lPXRd00-8&t=2561s) | 🟢 USEFUL | Follow-up: What is MPEG-DASH or adaptive streaming over HTTP? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [40:31](https://www.youtube.com/watch?v=35lPXRd00-8&t=2431s) because if you remember if you scroll up a little bit you'll notice that we were transferring the S across C with multiple different bit rates right so depending on that you would want to<br>[40:40](https://www.youtube.com/watch?v=35lPXRd00-8&t=2440s) ensure that whatever the network capacity is on the basis of that I should be presenting the user with that kind of stream uh data some of the other ones are Microsoft smooth streaming or | Adaptive HTTP streaming serves short encoded segments alongside a manifest describing available bitrates. The player can choose a rendition for its current network conditions. For example, a user changing from Wi-Fi to mobile data may switch quality between segments. Segment boundaries and compatible codecs are important to smooth playback. |

<a id="ia-59"></a>

## IA-59 — How does global upload latency differ from playback latency?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.48 | [43:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=2636s) | 🟢 USEFUL | How does global upload latency differ from playback latency? |
| YT-6.49 | [45:11](https://www.youtube.com/watch?v=35lPXRd00-8&t=2711s) | 🟢 USEFUL | Follow-up: How does global upload latency differ from playback latency? |
| YT-6.50 | [46:20](https://www.youtube.com/watch?v=35lPXRd00-8&t=2780s) | 🟢 USEFUL | Follow-up: How does global upload latency differ from playback latency? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [44:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=2658s) up going to go to the original storage which is your local cloud storage right it could be like a Google Cloud Storage or any S3 bucket whatever is happening in the background it's that part will<br>[44:28](https://www.youtube.com/watch?v=35lPXRd00-8&t=2668s) not be reflected to the user because it's like a background process you can you can just say that I click on a upload video button and just I upload my video with an indication that this job | Uploads may originate far from the central processing region, while playback should usually come from a nearby cache. For example, a creator in Asia can use a regional upload entry point, while viewers in Europe fetch finished videos from a European edge. These flows have different optimizations and failure modes. |

<a id="ia-60"></a>

## IA-60 — How would you collect video engagement signals for recommendations?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.51 | [46:55](https://www.youtube.com/watch?v=35lPXRd00-8&t=2815s) | 🟢 USEFUL | How would you collect video engagement signals for recommendations? |
| YT-6.52 | [48:06](https://www.youtube.com/watch?v=35lPXRd00-8&t=2886s) | 🟢 USEFUL | Follow-up: How would you collect video engagement signals for recommendations? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [47:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=2836s) the user next once this video has been completely watched overall understood so you will have it in parallel way do we need any synchronous communication between them because<br>[47:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=2847s) these are two different complete systems recommendation service and the CDN with the user analytics so we can do it in right we can do it in parall absolutely so synchronization comes into the play | Playback events such as impressions, watch time, completion, and likes can feed an analytics pipeline. For example, watching most of a tutorial may signal stronger interest than clicking and leaving after two seconds. I collect events asynchronously and protect user privacy. The recommender consumes aggregated signals rather than blocking playback. |

<a id="ia-61"></a>

## IA-61 — How do you keep popular videos hot in a CDN cache?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.53 | [48:32](https://www.youtube.com/watch?v=35lPXRd00-8&t=2912s) | 🟢 USEFUL | How do you keep popular videos hot in a CDN cache? |
| YT-6.54 | [49:41](https://www.youtube.com/watch?v=35lPXRd00-8&t=2981s) | 🟢 USEFUL | Follow-up: How do you keep popular videos hot in a CDN cache? |
| YT-6.55 | [50:49](https://www.youtube.com/watch?v=35lPXRd00-8&t=3049s) | 🟢 USEFUL | Follow-up: How do you keep popular videos hot in a CDN cache? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [48:44](https://www.youtube.com/watch?v=35lPXRd00-8&t=2924s) space for cost optimization one you have given me that we can use CDN for upload servers for Speedy uploads but you can use it only when there's a large amount of data I can go with that cost<br>[48:56](https://www.youtube.com/watch?v=35lPXRd00-8&t=2936s) optimization also here we have CDN uh and this CDN is the same here we have for the user viewers and from here we can quickly get the data to CL but CDN SSP s is very costly stuff so any | Popular segments are likely to be served repeatedly, so CDNs naturally cache them, and teams can tune cache headers or prewarm selected content. For example, a highly anticipated trailer benefits from early distribution. I'd monitor hit rate and origin traffic rather than manually copying every video to every edge. |

<a id="ia-62"></a>

## IA-62 — How would you build creator analytics for views and watch time?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.56 | [51:18](https://www.youtube.com/watch?v=35lPXRd00-8&t=3078s) | 🟢 USEFUL | How would you build creator analytics for views and watch time? |
| YT-6.57 | [52:24](https://www.youtube.com/watch?v=35lPXRd00-8&t=3144s) | 🟢 USEFUL | Follow-up: How would you build creator analytics for views and watch time? |
| YT-6.58 | [53:38](https://www.youtube.com/watch?v=35lPXRd00-8&t=3218s) | 🟢 USEFUL | Follow-up: How would you build creator analytics for views and watch time? |
| YT-6.59 | [54:51](https://www.youtube.com/watch?v=35lPXRd00-8&t=3291s) | 🟢 USEFUL | Follow-up: How would you build creator analytics for views and watch time? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [51:31](https://www.youtube.com/watch?v=35lPXRd00-8&t=3091s) engagements uh overall so let's let's call it as video engagements okay and video engagements is solely going to be interacting with the client uh uh over here with whatever video is<br>[51:47](https://www.youtube.com/watch?v=35lPXRd00-8&t=3107s) being processed as such so it is important for video engagements to be available to the user who's uploading the video because as a Creator you would want to know that how how folks are | I ingest viewing events, aggregate them by video and time window, and expose reports to creators. For example, a creator sees daily views, average watch time, and audience retention. Aggregated dashboards can be eventually consistent. Keeping analytics off the critical playback path helps reliability. |

<a id="ia-63"></a>

## IA-63 — How do likes, comments, and click-through rate influence recommendations?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.60 | [55:05](https://www.youtube.com/watch?v=35lPXRd00-8&t=3305s) | 🟢 USEFUL | How do likes, comments, and click-through rate influence recommendations? |
| YT-6.61 | [56:22](https://www.youtube.com/watch?v=35lPXRd00-8&t=3382s) | 🟢 USEFUL | Follow-up: How do likes, comments, and click-through rate influence recommendations? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [55:24](https://www.youtube.com/watch?v=35lPXRd00-8&t=3324s) other recommendation things are there for example how many times a person is clicking onto a video which is coming from a recommendation service so that sort of information also needs to be<br>[55:35](https://www.youtube.com/watch?v=35lPXRd00-8&t=3335s) captured somewhere right we so cannot solely rely on uh how many likes or how many on on the trend basically because recommendation is a very usern Niche sort of a thing so in fact we will have | Different signals mean different things: a click suggests interest, watch time reflects sustained attention, and likes or comments show engagement. For example, a clickbait title may get clicks but poor retention, so recommendations need multiple signals. A good system also considers freshness, user preferences, and harmful feedback loops. |

<a id="ia-64"></a>

## IA-64 — How would you store video thumbnails and generate previews?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.62 | [56:54](https://www.youtube.com/watch?v=35lPXRd00-8&t=3414s) | 🟢 USEFUL | How would you store video thumbnails and generate previews? |
| YT-6.63 | [58:04](https://www.youtube.com/watch?v=35lPXRd00-8&t=3484s) | 🟢 USEFUL | Follow-up: How would you store video thumbnails and generate previews? |
| YT-6.64 | [59:14](https://www.youtube.com/watch?v=35lPXRd00-8&t=3554s) | 🟢 USEFUL | Follow-up: How would you store video thumbnails and generate previews? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [57:08](https://www.youtube.com/watch?v=35lPXRd00-8&t=3428s) which what kind of image are we showing for that particular video and this I think is also supposed to be accounted for when we to deal with the video engagements and the same thing needs to<br>[57:17](https://www.youtube.com/watch?v=35lPXRd00-8&t=3437s) be shown to the user as well so I would say it also has to have a link uh actually instead of keeping it over here I would want to keep keep it over here wherein once the videos which has | Thumbnails are small image assets stored separately from large video streams, typically in object storage and served through a CDN. For example, a preview image can be generated during processing and associated with a video ID. Keeping them cacheable avoids hitting the metadata database for every image request. |

<a id="ia-65"></a>

## IA-65 — What are codecs and why do they matter to video platforms?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.65 | [1:00:02](https://www.youtube.com/watch?v=35lPXRd00-8&t=3602s) | 🟢 USEFUL | What are codecs and why do they matter to video platforms? |
| YT-6.66 | [1:01:10](https://www.youtube.com/watch?v=35lPXRd00-8&t=3670s) | 🟢 USEFUL | Follow-up: What are codecs and why do they matter to video platforms? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:00:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=3616s) there are like multiple people across the globe having different kind of devices uploading different kind of video qualities and they're all getting stored into a standardized format<br>[1:00:25](https://www.youtube.com/watch?v=35lPXRd00-8&t=3625s) because you YouTube works on a standardized format of showing the videos right so we'll have to uh account for that factor over here as well so when we record a video the video file is | A codec encodes and decodes audio or video into a transportable format. For example, H.264 is widely compatible, while other codecs can offer better compression but require device support. A platform may produce several compatible renditions. Codec choice trades bandwidth, quality, processing cost, and compatibility. |

<a id="ia-66"></a>

## IA-66 — How do bitrate, frame rate, and resolution affect video storage?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.67 | [1:02:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=3735s) | 🟢 USEFUL | How do bitrate, frame rate, and resolution affect video storage? |
| YT-6.68 | [1:03:22](https://www.youtube.com/watch?v=35lPXRd00-8&t=3802s) | 🟢 USEFUL | Follow-up: How do bitrate, frame rate, and resolution affect video storage? |
| YT-6.69 | [1:04:32](https://www.youtube.com/watch?v=35lPXRd00-8&t=3872s) | 🟢 USEFUL | Follow-up: How do bitrate, frame rate, and resolution affect video storage? |
| YT-6.70 | [1:05:44](https://www.youtube.com/watch?v=35lPXRd00-8&t=3944s) | 🟢 USEFUL | Follow-up: How do bitrate, frame rate, and resolution affect video storage? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:02:28](https://www.youtube.com/watch?v=35lPXRd00-8&t=3748s) is a computationally expensive and timec consuming process and besides this like different content creators may have different video processing requirements so for example some content creators<br>[1:02:38](https://www.youtube.com/watch?v=35lPXRd00-8&t=3758s) require watermarks on top of their videos some provide thumbnail images themselves like you said some has to have higher definition videos where other eyes do not have that information | Resolution describes picture dimensions, frame rate describes frames per second, and bitrate describes data sent per second. For example, two 1080p videos can have very different sizes if encoded at different bitrates. I estimate actual storage using bitrate times duration rather than assuming every frame takes a fixed number of megabytes. |

<a id="ia-67"></a>

## IA-67 — How do background workers process video transcoding jobs reliably?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.71 | [1:06:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=3975s) | 🟢 USEFUL | How do background workers process video transcoding jobs reliably? |
| YT-6.72 | [1:07:34](https://www.youtube.com/watch?v=35lPXRd00-8&t=4054s) | 🟢 USEFUL | Follow-up: How do background workers process video transcoding jobs reliably? |
| YT-6.73 | [1:08:42](https://www.youtube.com/watch?v=35lPXRd00-8&t=4122s) | 🟢 USEFUL | Follow-up: How do background workers process video transcoding jobs reliably? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:06:29](https://www.youtube.com/watch?v=35lPXRd00-8&t=3989s) for Me overall so the original video like I like we can see has been split across three different pipelines the audio video and the metadata part some of the tasks can be applied on a video<br>[1:06:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=3999s) file which are thumbnail inspection video trans codings and watermarks and whatnot and the other part would be the audio processing which is happening independently and then the metadata part | I enqueue an upload-completed job, let workers generate renditions, and persist job state. For example, a worker crash should allow retry without duplicating the final output. I use job IDs, idempotent writes, bounded retries, and dead-letter handling. Transcoding is expensive, so work must be recoverable. |

<a id="ia-68"></a>

## IA-68 — What components make up a video transcoding architecture?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.74 | [1:09:23](https://www.youtube.com/watch?v=35lPXRd00-8&t=4163s) | 🟢 USEFUL | What components make up a video transcoding architecture? |
| YT-6.75 | [1:10:43](https://www.youtube.com/watch?v=35lPXRd00-8&t=4243s) | 🟢 USEFUL | Follow-up: What components make up a video transcoding architecture? |
| YT-6.76 | [1:11:49](https://www.youtube.com/watch?v=35lPXRd00-8&t=4309s) | 🟢 USEFUL | Follow-up: What components make up a video transcoding architecture? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:09:37](https://www.youtube.com/watch?v=35lPXRd00-8&t=4177s) three or four different responsibilities which could be video splitting uh in terms of multiple uh you know chunk or frames yeah right group of pictures basically and second thing could be some<br>[1:09:51](https://www.youtube.com/watch?v=35lPXRd00-8&t=4191s) uh split video splitting would also be accounting for the fact that some older device not be able to support the video so we have to account for the devices that it should be compatible in terms of | A transcoding workflow can include preprocessing, task scheduling, workers, and assembly of finished segments. For example, one uploaded video is divided into tasks for 360p and 720p, processed in parallel, and then assembled. Keeping tasks independent helps scale expensive encoding work without blocking the upload API. |

<a id="ia-69"></a>

## IA-69 — How do job queues and priorities control video transcoding work?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.77 | [1:12:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=4347s) | 🟢 USEFUL | How do job queues and priorities control video transcoding work? |
| YT-6.78 | [1:13:37](https://www.youtube.com/watch?v=35lPXRd00-8&t=4417s) | 🟢 USEFUL | Follow-up: How do job queues and priorities control video transcoding work? |
| YT-6.79 | [1:14:47](https://www.youtube.com/watch?v=35lPXRd00-8&t=4487s) | 🟢 USEFUL | Follow-up: How do job queues and priorities control video transcoding work? |
| YT-6.80 | [1:16:03](https://www.youtube.com/watch?v=35lPXRd00-8&t=4563s) | 🟢 USEFUL | Follow-up: How do job queues and priorities control video transcoding work? |
| YT-6.81 | [1:17:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=4636s) | 🟢 USEFUL | Follow-up: How do job queues and priorities control video transcoding work? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:12:40](https://www.youtube.com/watch?v=35lPXRd00-8&t=4360s) of uh uh you know if if a particular task needs to be processed before the other task so whatever kind of uh uh priorities we're dealing about that part part will be taken care of my resource<br>[1:12:52](https://www.youtube.com/watch?v=35lPXRd00-8&t=4372s) manager and it will be Subs quently adding the task to maybe a task que or a worker queue or a running queue or a priority queue depending upon what is the priority we're looking at and | A task queue carries work identifiers and priority rather than a huge video file. For example, a resource manager can give a small urgent conversion higher priority while workers process ordinary encodings. I track retries and completion separately. Queues make processing capacity independent of the upload servers. |

<a id="ia-70"></a>

## IA-70 — How can presigned URLs safely authorize media uploads or downloads?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.82 | [1:17:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=4659s) | 🟢 USEFUL | How can presigned URLs safely authorize media uploads or downloads? |
| YT-6.83 | [1:18:55](https://www.youtube.com/watch?v=35lPXRd00-8&t=4735s) | 🟢 USEFUL | Follow-up: How can presigned URLs safely authorize media uploads or downloads? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:17:51](https://www.youtube.com/watch?v=35lPXRd00-8&t=4671s) for the safety optimization like a pre pre-signed URL which from which we can fetch the data information so that's also something we have to be accounting for over here<br>[1:18:01](https://www.youtube.com/watch?v=35lPXRd00-8&t=4681s) perfect perfect that's that's the Privacy that you're maintaining with your videos that is uploading and downloading here and there that's right that's right perfect uh I think pretty much we have | A presigned URL provides temporary access to one object operation without giving clients permanent cloud credentials. For example, a user can upload a specific media object directly to storage for a short period. I restrict its lifetime, operation, and object key. Backend authorization happens before issuing the URL. |
