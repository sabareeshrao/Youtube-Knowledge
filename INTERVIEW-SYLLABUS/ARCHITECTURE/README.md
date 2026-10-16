# System Design / Architecture interview syllabus

**85 permanent interview questions.** ⭐ marks a question covered in more than one source video.

| ID | Question | Video options |
|---|---|---|
| [IA-1](IA-1.md) | Explain cache-aside caching using Redis and a database. | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-2](IA-2.md) | How would you control stale cached data using TTL and consistency requirements? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-3](IA-3.md) | When would you choose GraphQL over REST for an API? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-4](IA-4.md) | How does GraphQL field selection compare with REST DTO responses? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-5](IA-5.md) ⭐ | Compare Saga and two-phase commit for distributed microservice transactions. | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) · [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-6](IA-6.md) | How would you gather functional and nonfunctional requirements for an e-commerce platform? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-7](IA-7.md) | How would you protect e-commerce APIs from abusive traffic and request floods? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-8](IA-8.md) | Design a load-balanced high-level architecture for a large e-commerce application. | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-9](IA-9.md) | Design product search using a cache, database and search index. | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-10](IA-10.md) | How would you model a user's cart, and why might you choose a relational database? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-11](IA-11.md) ⭐ | How should cart, product, inventory and user responsibilities be split across services? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-12](IA-12.md) | How do you avoid overselling the last inventory item when Kafka delivery is delayed? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-13](IA-13.md) | How would you implement delivery-partner assignment with asynchronous events? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-14](IA-14.md) | How would you deliver order-status notifications by email and SMS? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-15](IA-15.md) | Design an event-driven order-tracking system with a suitable database. | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-16](IA-16.md) | What data would you collect for logs and commerce analytics? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-17](IA-17.md) | Why use a CDN for an e-commerce product catalog? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-18](IA-18.md) ⭐ | How would you autoscale services when traffic surges during holiday sales? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-19](IA-19.md) | How would you implement infinite scroll with pagination, prefetching and loading feedback? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-20](IA-20.md) ⭐ | How would you diagnose Kafka consumer lag in a distributed system? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) · [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) |
| [IA-21](IA-21.md) ⭐ | How would backend microservices communicate with each other using HTTP clients? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-22](IA-22.md) | What tradeoffs affect choosing a database for search versus shopping-cart data? | [YT-1](../../VIDEO-LIBRARY/YT-1/timestamps.md) |
| [IA-23](IA-23.md) | Why do microservices need service registration and discovery? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-24](IA-24.md) | How is client-side load balancing related to service discovery? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-25](IA-25.md) | Why is discovery especially valuable in cloud deployments? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-26](IA-26.md) | How do you avoid a single point of failure in service discovery? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-27](IA-27.md) | Why use an API gateway in front of microservices? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-28](IA-28.md) | How do synchronous HTTP and asynchronous messaging differ between services? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-29](IA-29.md) | How would you reduce latency between microservices? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-30](IA-30.md) | How do you publish REST API documentation to consumers? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-31](IA-31.md) | How do you version a REST API without breaking old clients? | [YT-3](../../VIDEO-LIBRARY/YT-3/timestamps.md) |
| [IA-32](IA-32.md) | How do Saga orchestration and choreography compare? | [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) |
| [IA-33](IA-33.md) | How do an API gateway, service discovery, and load balancing differ? | [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) |
| [IA-34](IA-34.md) ⭐ | What does the SOLID single-responsibility principle mean? | [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) · [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-35](IA-35.md) ⭐ | How does the open-closed principle apply to payment integrations? | [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) · [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) |
| [IA-36](IA-36.md) | What are Kafka topics, partitions, and consumer groups? | [YT-4](../../VIDEO-LIBRARY/YT-4/timestamps.md) |
| [IA-37](IA-37.md) | What do the five SOLID principles try to improve? | [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) |
| [IA-38](IA-38.md) | What is the interface segregation principle? | [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) |
| [IA-39](IA-39.md) | What is dependency inversion and how does Spring help? | [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) |
| [IA-40](IA-40.md) ⭐ | When would you choose Factory, Singleton, or Builder patterns? | [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) · [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-41](IA-41.md) | How does the Builder pattern help create objects? | [YT-5](../../VIDEO-LIBRARY/YT-5/timestamps.md) |
| [IA-42](IA-42.md) | How would you define functional requirements for a YouTube-like service? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-43](IA-43.md) | Which nonfunctional requirements matter for a video platform? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-44](IA-44.md) | How would you estimate daily active users and video viewing volume? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-45](IA-45.md) | How do you estimate daily video storage requirements? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-46](IA-46.md) | How would you estimate CDN bandwidth and delivery costs? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-47](IA-47.md) | How does autoscaling help a video streaming service? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-48](IA-48.md) | Why are replication and fault tolerance important for video data? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-49](IA-49.md) | How would you make large video uploads resumable? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-50](IA-50.md) | Why does video transcoding produce multiple resolutions and bitrates? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-51](IA-51.md) | How does adaptive bitrate streaming avoid long playback delays? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-52](IA-52.md) | How would you detect and retry missing video upload chunks? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-53](IA-53.md) | What services participate in an end-to-end video upload pipeline? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-54](IA-54.md) | Why deliver processed videos through a CDN? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-55](IA-55.md) | How would you manage video upload status and completion notifications? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-56](IA-56.md) | How can a video ID route a request to the correct metadata shard? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-57](IA-57.md) | How would you design the watch-video request path? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-58](IA-58.md) | What is MPEG-DASH or adaptive streaming over HTTP? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-59](IA-59.md) | How does global upload latency differ from playback latency? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-60](IA-60.md) | How would you collect video engagement signals for recommendations? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-61](IA-61.md) | How do you keep popular videos hot in a CDN cache? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-62](IA-62.md) | How would you build creator analytics for views and watch time? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-63](IA-63.md) | How do likes, comments, and click-through rate influence recommendations? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-64](IA-64.md) | How would you store video thumbnails and generate previews? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-65](IA-65.md) | What are codecs and why do they matter to video platforms? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-66](IA-66.md) | How do bitrate, frame rate, and resolution affect video storage? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-67](IA-67.md) | How do background workers process video transcoding jobs reliably? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-68](IA-68.md) | What components make up a video transcoding architecture? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-69](IA-69.md) | How do job queues and priorities control video transcoding work? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-70](IA-70.md) | How can presigned URLs safely authorize media uploads or downloads? | [YT-6](../../VIDEO-LIBRARY/YT-6/timestamps.md) |
| [IA-71](IA-71.md) | How does an Angular-to-Spring Boot API request travel through the layers? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-72](IA-72.md) | How does Angular property binding differ from event binding? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-73](IA-73.md) | What do interpolation and two-way binding mean in Angular? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-74](IA-74.md) | Why is Angular called a single-page application framework? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-75](IA-75.md) | Why use TypeScript instead of plain JavaScript in Angular? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-76](IA-76.md) | What are Angular selectors, templates, and styles? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-77](IA-77.md) | What are built-in and custom Angular pipes? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-78](IA-78.md) | How do Angular AOT and JIT compilation differ? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-79](IA-79.md) | How do JavaScript Promises compare with RxJS Observables? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-80](IA-80.md) | How do Angular components share data with one another? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-81](IA-81.md) | How does Angular Router switch views without a full reload? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-82](IA-82.md) | What are Angular HTTP interceptors used for? | [YT-7](../../VIDEO-LIBRARY/YT-7/timestamps.md) |
| [IA-83](IA-83.md) | What does a circuit breaker and fallback do when a service fails? | [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-84](IA-84.md) | How do OpenFeign and RestTemplate differ? | [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |
| [IA-85](IA-85.md) | When is asynchronous messaging better than a direct REST call? | [YT-8](../../VIDEO-LIBRARY/YT-8/timestamps.md) |

[All subjects](../README.md) · [Video library](../../INDEX.md)
