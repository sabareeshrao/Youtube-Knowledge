# YT-1 — Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Original video:** https://www.youtube.com/watch?v=xMlcsFLk-CU  
**Source transcript:** [transcript.md](transcript.md)  
**Source length:** last subtitle begins at 1:34:38  
**Sections:** 134 (chronological; opening timestamps only)

This page is the **independent timeline for YT-1 only**. Green = useful, yellow = introduction, red = skip. All subtitles, including skipped ones, remain in the [original transcript](transcript.md).

## Chronological topic navigation

<a id="yt-1-1"></a>
### YT-1.1 — [0:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=0s) — 🔴 NO NEED: Opening promotions and channel announcements

The host introduces the mock interview and promotes sign-up and resume-review forms.

<a id="yt-1-2"></a>
### YT-1.2 — [1:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=90s) — 🟡 INTRO: Candidate introduction

The interviewer asks the candidate to introduce himself; the candidate discusses moving to Canada.

<a id="yt-1-3"></a>
### YT-1.3 — [2:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=120s) — 🟡 INTRO: Experience and technology stack

The candidate mentions Java, Spring Boot, React, Node.js and other prior work.

<a id="yt-1-4"></a>
### YT-1.4 — [2:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) — 🟢 USEFUL: Spring Security end-to-end question

The interviewer asks how security is implemented from frontend through backend.

<a id="yt-1-5"></a>
### YT-1.5 — [3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) — 🟢 USEFUL: Stateless REST and JWT

The candidate discusses JWT for stateless REST API authentication.

<a id="yt-1-6"></a>
### YT-1.6 — [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) — 🟢 USEFUL: Token expiration and refresh tokens

Short-lived token expiration and refresh-token handling are raised.

<a id="yt-1-7"></a>
### YT-1.7 — [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) — 🟢 USEFUL: Okta OAuth authorization server

Discussion of Okta, OAuth 2.0 and Spring Security integration.

**Terms or identifiers spoken:** Okta, OAuth 2.0, Spring Security

<a id="yt-1-8"></a>
### YT-1.8 — [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) — 🟢 USEFUL: Authentication redirect and authorization flow

The interviewer probes where Okta is called, login screens, access tokens and grant types.

<a id="yt-1-9"></a>
### YT-1.9 — [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) — 🟢 USEFUL: Callback URLs and identity-provider configuration

The candidate explains login redirects and configuration at a high level.

<a id="yt-1-10"></a>
### YT-1.10 — [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) — 🟢 USEFUL: Frontend-to-Okta-to-backend flow

The interviewer summarizes how frontend authentication leads to backend API calls.

<a id="yt-1-11"></a>
### YT-1.11 — [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) — 🟢 USEFUL: How a backend validates JWTs

A forged-token scenario prompts questions on JWT verification.

<a id="yt-1-12"></a>
### YT-1.12 — [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) — 🟢 USEFUL: JWT signature and payload discussion

The candidate describes JWT parts and a signature used to detect tampering.

**Accuracy note (independent review):** JWT payloads are commonly base64url-encoded rather than encrypted. Signing verifies integrity; never store passwords in the payload.

<a id="yt-1-13"></a>
### YT-1.13 — [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) — 🟢 USEFUL: Questionable JWT validation explanation

The candidate discusses checking decoded data against database values; verify this independently.

**Accuracy note (independent review):** The described database/hash reversal is not standard JWT verification. Verify signature, issuer, audience, expiry and other applicable claims using a trusted library.

<a id="yt-1-14"></a>
### YT-1.14 — [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) — 🟢 USEFUL: Sensitive data inside JWT claims

The interviewer cautions against passwords and personal data in readable JWT payloads.

<a id="yt-1-15"></a>
### YT-1.15 — [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) — 🟢 USEFUL: Password and JWT payload safety

The participants emphasize avoiding sensitive values in token payloads.

<a id="yt-1-16"></a>
### YT-1.16 — [10:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=614s) — 🟡 INTRO: Transition from security to scheduling

The interviewer switches to scheduler implementations used in the application.

<a id="yt-1-17"></a>
### YT-1.17 — [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) — 🟢 USEFUL: Duplicate scheduled jobs across replicas

Three deployed instances can all execute the same Spring scheduled task and insert duplicate rows.

<a id="yt-1-18"></a>
### YT-1.18 — [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) — 🟢 USEFUL: ShedLock for single scheduler execution

The candidate proposes ShedLock-style distributed locking.

**Terms or identifiers spoken:** ShedLock

<a id="yt-1-19"></a>
### YT-1.19 — [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) — 🟡 INTRO: Caching discussion begins

The interview changes focus to caching in Spring applications.

<a id="yt-1-20"></a>
### YT-1.20 — [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) — 🟢 USEFUL: Redis cache-aside lookup

The candidate explains looking up frequent data in memory and falling back to the database on misses.

**Terms or identifiers spoken:** Redis

<a id="yt-1-21"></a>
### YT-1.21 — [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) — 🟢 USEFUL: In-memory caching and latency

The interviewer asks what an in-memory cache means near the application.

<a id="yt-1-22"></a>
### YT-1.22 — [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) — 🟢 USEFUL: Cache TTL and freshness

The candidate describes temporary cache entries and time-to-live.

<a id="yt-1-23"></a>
### YT-1.23 — [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) — 🟢 USEFUL: Stale cached data and TTL tradeoffs

The interviewer probes stale responses and excessive database traffic with very short TTLs.

<a id="yt-1-24"></a>
### YT-1.24 — [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) — 🟢 USEFUL: Cache consistency requirements

The discussion considers how staleness may be acceptable for some products but not others.

<a id="yt-1-25"></a>
### YT-1.25 — [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) — 🟢 USEFUL: Financial data and eventual consistency

Account balances are offered as a counterexample to casually accepting stale reads.

<a id="yt-1-26"></a>
### YT-1.26 — [14:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=886s) — 🟡 INTRO: Transition to Hibernate caching

The interviewer asks whether Hibernate caching has been implemented.

<a id="yt-1-27"></a>
### YT-1.27 — [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) — 🟢 USEFUL: JPA/Hibernate entity caching

The candidate introduces JPA implementations and first- and second-level caching.

**Terms or identifiers spoken:** JPA, Hibernate

<a id="yt-1-28"></a>
### YT-1.28 — [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) — 🟢 USEFUL: Compare Hibernate L1 and L2 caching

The interviewer asks which cache belongs to the Session versus SessionFactory.

**Terms or identifiers spoken:** Session, SessionFactory

<a id="yt-1-29"></a>
### YT-1.29 — [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) — 🟢 USEFUL: Default L1 and opt-in L2 cache

The candidate identifies first-level session caching and cross-session second-level caching.

<a id="yt-1-30"></a>
### YT-1.30 — [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) — 🟢 USEFUL: Second-level cache beyond Session lifetime

An entity may remain cached at the shared second level after an individual Session closes.

<a id="yt-1-31"></a>
### YT-1.31 — [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) — 🟢 USEFUL: Why SessionFactory is expensive and shared

The interviewer asks why SessionFactory is usually reused rather than frequently created.

<a id="yt-1-32"></a>
### YT-1.32 — [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) — 🟢 USEFUL: Multiple databases and SessionFactory instances

The interviewer poses Oracle, MySQL and PostgreSQL in one application.

<a id="yt-1-33"></a>
### YT-1.33 — [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) — 🟢 USEFUL: Why GraphQL instead of REST

The interviewer asks for the use cases that motivate GraphQL.

<a id="yt-1-34"></a>
### YT-1.34 — [19:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1145s) — 🟢 USEFUL: GraphQL query entry point

The candidate describes exposing a GraphQL endpoint and client-requested data.

<a id="yt-1-35"></a>
### YT-1.35 — [19:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1169s) — 🟢 USEFUL: GraphQL versus REST decision criteria

The interviewer requests an actual design scenario and trade-off.

<a id="yt-1-36"></a>
### YT-1.36 — [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) — 🟢 USEFUL: GraphQL field-level selection

A large Employee response prompts the question of selecting only ID and name.

**Terms or identifiers spoken:** GraphQL

<a id="yt-1-37"></a>
### YT-1.37 — [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) — 🟢 USEFUL: REST DTO and field filtering alternatives

The candidate mentions DTO selection and JSON serialization controls.

**Terms or identifiers spoken:** DTO, JsonIgnore

<a id="yt-1-38"></a>
### YT-1.38 — [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) — 🟢 USEFUL: Variable response fields across clients

The interviewer contrasts dynamic GraphQL selections with fixed REST DTO designs.

<a id="yt-1-39"></a>
### YT-1.39 — [22:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1359s) — 🟢 USEFUL: External Spring Boot configuration

The discussion moves to application properties and YAML.

<a id="yt-1-40"></a>
### YT-1.40 — [23:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1380s) — 🟢 USEFUL: Properties versus YAML

The interviewer asks which configuration format is better and why.

**Terms or identifiers spoken:** application.properties, application.yml

<a id="yt-1-41"></a>
### YT-1.41 — [23:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1418s) — 🟢 USEFUL: Hierarchical YAML configuration

The candidate explains nesting under a common prefix instead of repeating property keys.

<a id="yt-1-42"></a>
### YT-1.42 — [24:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1453s) — 🟢 USEFUL: Structured configuration values

YAML collections and maps are discussed alongside properties.

<a id="yt-1-43"></a>
### YT-1.43 — [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) — 🟢 USEFUL: Distributed transactions in microservices

The interviewer asks how to coordinate changes across independently committed services.

<a id="yt-1-44"></a>
### YT-1.44 — [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) — 🟢 USEFUL: Saga versus two-phase commit

The candidate introduces saga-style execution and 2PC as alternatives.

<a id="yt-1-45"></a>
### YT-1.45 — [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) — 🟢 USEFUL: Saga events and compensating actions

The candidate describes publishing events and reversing completed local operations after failure.

<a id="yt-1-46"></a>
### YT-1.46 — [25:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1555s) — 🟡 INTRO: E-commerce system-design prompt

The interviewer asks for a high-level e-commerce architecture.

<a id="yt-1-47"></a>
### YT-1.47 — [26:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1618s) — 🟢 USEFUL: Functional e-commerce requirements

Shopping, search, cart and checkout are selected as functional capabilities.

<a id="yt-1-48"></a>
### YT-1.48 — [27:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1655s) — 🟢 USEFUL: Nonfunctional requirements

Scale, resilience and response latency are introduced.

<a id="yt-1-49"></a>
### YT-1.49 — [28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1717s) — 🟢 USEFUL: Search, cart, order, delivery and notification scope

The interviewer formalizes core functional capabilities for the system.

<a id="yt-1-50"></a>
### YT-1.50 — [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) — 🟢 USEFUL: Abusive traffic and peak sale load

The interviewer asks how to resist repeated spam-like requests and peak traffic.

<a id="yt-1-51"></a>
### YT-1.51 — [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) — 🟢 USEFUL: Client and web/mobile system entry point

The candidate begins drawing client-side interactions.

<a id="yt-1-52"></a>
### YT-1.52 — [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) — 🟢 USEFUL: Load balancers for replicated services

Load balancing distributes requests among application replicas.

<a id="yt-1-53"></a>
### YT-1.53 — [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) — 🟢 USEFUL: Nginx reverse proxy and load balancing

Nginx is suggested as a reverse proxy/load balancer.

<a id="yt-1-54"></a>
### YT-1.54 — [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) — 🟢 USEFUL: Rate limiting suspicious requests

Request thresholds or per-IP limits are suggested against excessive hits.

<a id="yt-1-55"></a>
### YT-1.55 — [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) — 🟢 USEFUL: Search service and microservice boundary

The load balancer routes incoming searches to backend service instances.

<a id="yt-1-56"></a>
### YT-1.56 — [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) — 🟢 USEFUL: Redis cache for product search

Caching frequently queried product information is introduced.

<a id="yt-1-57"></a>
### YT-1.57 — [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) — 🟢 USEFUL: NoSQL choices for product search

Cassandra and MongoDB are discussed as possible data stores.

<a id="yt-1-58"></a>
### YT-1.58 — [36:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2165s) — 🟢 USEFUL: Elasticsearch for product queries

The candidate adds search indexing alongside the product data store.

<a id="yt-1-59"></a>
### YT-1.59 — [37:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2259s) — 🟢 USEFUL: Text search and typo-tolerant indexing

Keywords and search-index matching are discussed.

<a id="yt-1-60"></a>
### YT-1.60 — [38:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2297s) — 🟢 USEFUL: Hot search queries cached in Redis

Frequently searched results may be served from cache.

<a id="yt-1-61"></a>
### YT-1.61 — [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) — 🟢 USEFUL: Cart service data model

The candidate explains user-to-cart item mappings.

<a id="yt-1-62"></a>
### YT-1.62 — [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) — 🟢 USEFUL: SQL database choice for cart

Relational storage and consistency arguments are discussed.

<a id="yt-1-63"></a>
### YT-1.63 — [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) — 🟢 USEFUL: Service-to-service communication

The candidate mentions REST/Feign-style interactions among services.

<a id="yt-1-64"></a>
### YT-1.64 — [41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) — 🟢 USEFUL: Order and delivery business workflow

Order placement, payment and fulfillment span multiple responsibilities.

<a id="yt-1-65"></a>
### YT-1.65 — [42:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2521s) — 🟢 USEFUL: Kafka events and inventory reduction

The initial design considers Kafka after an order to update inventory.

<a id="yt-1-66"></a>
### YT-1.66 — [42:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2561s) — 🟢 USEFUL: Overselling due to delayed consumers

The interviewer points out that asynchronous inventory reduction can oversell limited stock.

<a id="yt-1-67"></a>
### YT-1.67 — [43:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2599s) — 🟢 USEFUL: Inventory consistency reconsidered

The candidate acknowledges the race and discusses stricter stock-control requirements.

<a id="yt-1-68"></a>
### YT-1.68 — [43:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2638s) — 🟢 USEFUL: Inventory and product service split

Inventory, cart, user and product responsibilities are separated.

<a id="yt-1-69"></a>
### YT-1.69 — [44:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2683s) — 🟢 USEFUL: Single responsibility for product service

The interviewer argues for distinct product and user services.

<a id="yt-1-70"></a>
### YT-1.70 — [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) — 🟢 USEFUL: Assigning delivery partners

The system design adds a delivery assignment component.

<a id="yt-1-71"></a>
### YT-1.71 — [46:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2765s) — 🟢 USEFUL: Structured delivery partner storage

The candidate proposes SQL data storage for partner details.

<a id="yt-1-72"></a>
### YT-1.72 — [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) — 🟢 USEFUL: Saga is not one global ACID transaction

The interviewer challenges the claim that Saga gives all-or-nothing database atomicity across services.

**Accuracy note (independent review):** Saga compensations do not create one globally atomic database transaction.

<a id="yt-1-73"></a>
### YT-1.73 — [48:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2896s) — 🟢 USEFUL: Delivery assignment need not be immediate

The interviewer separates order completion from eventual delivery assignment.

<a id="yt-1-74"></a>
### YT-1.74 — [48:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2930s) — 🟢 USEFUL: Kafka event-driven delivery processing

Delivery-partner services can consume order events after checkout.

<a id="yt-1-75"></a>
### YT-1.75 — [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) — 🟢 USEFUL: Email and SMS notifications

A notification service handles user preferences and message channels.

<a id="yt-1-76"></a>
### YT-1.76 — [50:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3000s) — 🟢 USEFUL: Order tracking requirement

The design adds a shipment/tracking workflow for customers.

<a id="yt-1-77"></a>
### YT-1.77 — [50:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3038s) — 🟢 USEFUL: Logs and sales analytics

Log storage and Spark-style analytics are briefly discussed.

<a id="yt-1-78"></a>
### YT-1.78 — [51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) — 🟢 USEFUL: Tracking events through Kafka

Order events are used to update tracking history.

<a id="yt-1-79"></a>
### YT-1.79 — [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) — 🟢 USEFUL: Choosing SQL for structured tracking rows

The interviewer asks why simple timestamp/status records would require NoSQL.

<a id="yt-1-80"></a>
### YT-1.80 — [53:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3195s) — 🟢 USEFUL: Delivery confirmation asynchronously

Kafka is proposed for marking items delivered after confirmation.

<a id="yt-1-81"></a>
### YT-1.81 — [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) — 🟢 USEFUL: Slow SQL query diagnosis

The interviewer introduces slow reads over large relational datasets.

<a id="yt-1-82"></a>
### YT-1.82 — [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) — 🟢 USEFUL: Indexing and query profiling

The candidate discusses query analysis and adding indexes.

<a id="yt-1-83"></a>
### YT-1.83 — [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) — 🟢 USEFUL: Database partitioning

Partitioning large datasets is mentioned as a possible scaling strategy.

<a id="yt-1-84"></a>
### YT-1.84 — [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) — 🟢 USEFUL: Sharding versus partitioning

The discussion contrasts data on different servers with partitioning within a database environment.

<a id="yt-1-85"></a>
### YT-1.85 — [55:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3359s) — 🟢 USEFUL: Kafka consumer lag question

The interviewer asks about messages pending for Kafka consumers; the candidate does not provide a concrete fix.

**Interview gap:** The transcript raises Kafka consumer lag but does not demonstrate a specific remediation procedure.

<a id="yt-1-86"></a>
### YT-1.86 — [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) — 🟢 USEFUL: CDN for images and static content

A content delivery network is proposed for product images and other assets.

<a id="yt-1-87"></a>
### YT-1.87 — [58:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3529s) — 🟢 USEFUL: Autoscaling during sales spikes

Cloud monitoring and thresholds can scale application instances up or down.

<a id="yt-1-88"></a>
### YT-1.88 — [59:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3592s) — 🟢 USEFUL: Backend and frontend pagination prompt

The interviewer asks how to display thousands of products.

<a id="yt-1-89"></a>
### YT-1.89 — [1:00:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3628s) — 🟢 USEFUL: Lazy loading and infinite scrolling

The candidate explains loading another page as a user scrolls.

<a id="yt-1-90"></a>
### YT-1.90 — [1:01:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3678s) — 🟢 USEFUL: JPA pagination and batch fetching

The backend is expected to fetch a bounded number of rows per request.

<a id="yt-1-91"></a>
### YT-1.91 — [1:01:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3719s) — 🟢 USEFUL: Latency between scrolling and API response

The interviewer asks how to hide the request gap.

<a id="yt-1-92"></a>
### YT-1.92 — [1:02:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3761s) — 🟢 USEFUL: Prefetching before viewport end

The candidate suggests loading before the bottom of the page becomes visible.

<a id="yt-1-93"></a>
### YT-1.93 — [1:03:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3786s) — 🟢 USEFUL: Skeleton states, debounce and throttle

The conversation mentions loading placeholders and controlling repeated user-triggered requests.

<a id="yt-1-94"></a>
### YT-1.94 — [1:03:51](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3831s) — 🟡 INTRO: Transition to Git branching and delivery

The interview switches from architecture to team workflow.

<a id="yt-1-95"></a>
### YT-1.95 — [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) — 🟢 USEFUL: Git branch, feature and promotion strategy

The candidate explains development, feature, QA, staging and production stages.

<a id="yt-1-96"></a>
### YT-1.96 — [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) — 🟢 USEFUL: Environment-specific configuration and profiles

The interviewer asks how source code changes between deployment environments.

<a id="yt-1-97"></a>
### YT-1.97 — [1:05:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3946s) — 🟢 USEFUL: Spring profiles with per-environment properties

Configuration for development, QA and production is discussed.

**Terms or identifiers spoken:** Spring profiles, application-dev, application-staging

<a id="yt-1-98"></a>
### YT-1.98 — [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) — 🟢 USEFUL: How commits trigger deployments

The interviewer probes what happens after a pull request merges.

<a id="yt-1-99"></a>
### YT-1.99 — [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) — 🟢 USEFUL: CI/CD definition and tool choices

Jenkins and GitHub Actions are referenced before differentiating integration from deployment.

<a id="yt-1-100"></a>
### YT-1.100 — [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) — 🟢 USEFUL: Continuous integration checks

Automated builds, JUnit/Selenium tests and merge gates are discussed.

<a id="yt-1-101"></a>
### YT-1.101 — [1:08:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4122s) — 🟢 USEFUL: Continuous delivery and deployment

The candidate describes automated packaging and deployment into environments.

<a id="yt-1-102"></a>
### YT-1.102 — [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) — 🟢 USEFUL: Dockerfile, image and container

The candidate describes a Dockerfile, bundled dependencies and a Java process.

**Terms or identifiers spoken:** Dockerfile

<a id="yt-1-103"></a>
### YT-1.103 — [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) — 🟢 USEFUL: Managing multiple microservice containers

The interviewer asks how to operate a fleet of containers.

<a id="yt-1-104"></a>
### YT-1.104 — [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) — 🟢 USEFUL: Kubernetes orchestration and replicas

Kubernetes is introduced for managing service workloads and scaling.

**Terms or identifiers spoken:** Kubernetes

<a id="yt-1-105"></a>
### YT-1.105 — [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) — 🟢 USEFUL: Repeated Kubernetes pod crashes

The interviewer presents a restart-loop production incident.

<a id="yt-1-106"></a>
### YT-1.106 — [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) — 🟢 USEFUL: Crash triage, logs and PagerDuty

The candidate discusses on-call response and diagnosing infrastructure or application causes.

<a id="yt-1-107"></a>
### YT-1.107 — [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) — 🟢 USEFUL: Rollback to previous application version

The interviewer emphasizes versioned releases and rollback.

<a id="yt-1-108"></a>
### YT-1.108 — [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) — 🟢 USEFUL: Release versioning and rollback workflow

The candidate discusses previous container images and restoring a working version.

<a id="yt-1-109"></a>
### YT-1.109 — [1:14:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4453s) — 🟢 USEFUL: Infrastructure as code with Pulumi

The discussion names Pulumi and Terraform as infrastructure-automation options.

**Terms or identifiers spoken:** Pulumi, Terraform

<a id="yt-1-110"></a>
### YT-1.110 — [1:14:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4481s) — 🟢 USEFUL: Azure alerting and infrastructure automation

The candidate mentions Azure resources and creating alert infrastructure.

<a id="yt-1-111"></a>
### YT-1.111 — [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) — 🟢 USEFUL: High test coverage question

The interviewer asks about a claimed 90–95 percent coverage level.

<a id="yt-1-112"></a>
### YT-1.112 — [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) — 🟢 USEFUL: JUnit tests and mocked dependencies

Unit tests, nested classes and mocks are discussed.

<a id="yt-1-113"></a>
### YT-1.113 — [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) — 🟢 USEFUL: SonarQube and static analysis

Coverage and source-code quality tooling are discussed.

**Terms or identifiers spoken:** SonarQube

<a id="yt-1-114"></a>
### YT-1.114 — [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) — 🟢 USEFUL: Do not test trivial getters just for coverage

The interviewer questions creating meaningless tests to increase a percentage.

<a id="yt-1-115"></a>
### YT-1.115 — [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) — 🟢 USEFUL: Exclude DTO boilerplate from coverage

The interview asks how to exclude low-value packages using test/build configuration.

**Terms or identifiers spoken:** Maven XML build configuration

<a id="yt-1-116"></a>
### YT-1.116 — [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) — 🟢 USEFUL: Integration tests for entities and services

The conversation distinguishes integration coverage from isolated unit tests.

<a id="yt-1-117"></a>
### YT-1.117 — [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) — 🟢 USEFUL: Microservice end-to-end testing

The interviewer discusses testing cart and order services together.

<a id="yt-1-118"></a>
### YT-1.118 — [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) — 🟢 USEFUL: Avoid real cross-service calls in unit tests

The interviewer points out the latency and dependencies of live API calls during builds.

<a id="yt-1-119"></a>
### YT-1.119 — [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) — 🟢 USEFUL: Use separate integration/system-test suites

The candidate and interviewer discuss exercising integrations separately from unit tests.

<a id="yt-1-120"></a>
### YT-1.120 — [1:22:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4951s) — 🟡 INTRO: Introduction to reactive Spring applications

The interviewer switches to Reactor and reactive processing.

<a id="yt-1-121"></a>
### YT-1.121 — [1:22:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4966s) — 🟢 USEFUL: Blocking versus nonblocking I/O

The candidate discusses threads waiting for responses versus callbacks.

<a id="yt-1-122"></a>
### YT-1.122 — [1:23:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5013s) — 🟢 USEFUL: Mono and Flux overview

The candidate identifies Reactor publishers for one or many results.

**Terms or identifiers spoken:** Mono, Flux

<a id="yt-1-123"></a>
### YT-1.123 — [1:23:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5032s) — 🟢 USEFUL: Project Reactor in Spring

The interview briefly mentions reactive libraries and dependency setup.

**Terms or identifiers spoken:** Project Reactor

<a id="yt-1-124"></a>
### YT-1.124 — [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) — 🟢 USEFUL: Maven versus Gradle question

The interviewer asks what Maven and Gradle do.

<a id="yt-1-125"></a>
### YT-1.125 — [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) — 🟢 USEFUL: Build tool choice and differences

Dependency/build tooling and perceived build-speed differences are discussed.

<a id="yt-1-126"></a>
### YT-1.126 — [1:25:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5136s) — 🟢 USEFUL: Purpose of pom.xml

The candidate describes dependency versions and fetching jars from repositories.

**Terms or identifiers spoken:** pom.xml

<a id="yt-1-127"></a>
### YT-1.127 — [1:26:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5212s) — 🟢 USEFUL: Kanban versus Scrum in team workflow

The interviewer asks about Kanban and how it relates to agile development.

<a id="yt-1-128"></a>
### YT-1.128 — [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) — 🟢 USEFUL: ConcurrentHashMap internal design question

The interviewer asks why and when concurrent maps are needed.

**Terms or identifiers spoken:** ConcurrentHashMap

<a id="yt-1-129"></a>
### YT-1.129 — [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) — 🟢 USEFUL: HashMap fail-fast iteration

The candidate discusses structural modification during iteration and exceptions.

<a id="yt-1-130"></a>
### YT-1.130 — [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) — 🟢 USEFUL: Concurrent access and synchronization

The interviewer asks how thread-safe concurrent operations are achieved.

<a id="yt-1-131"></a>
### YT-1.131 — [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) — 🟢 USEFUL: Legacy segment-lock explanation caveat

The participants describe segmented locking; implementation specifics are Java-version dependent.

**Accuracy note (independent review):** This segment-lock description reflects older implementation discussions; modern Java ConcurrentHashMap is not a simple fixed 16-segment structure.

<a id="yt-1-132"></a>
### YT-1.132 — [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) — 🟢 USEFUL: Using employee objects as HashMap keys

The interviewer asks how custom domain objects can safely be keys.

<a id="yt-1-133"></a>
### YT-1.133 — [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) — 🟢 USEFUL: equals and hashCode contract

The candidate identifies overriding both equality and hash-code methods.

**Terms or identifiers spoken:** equals(), hashCode()

<a id="yt-1-134"></a>
### YT-1.134 — [1:32:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5532s) — 🔴 NO NEED: Interview feedback and farewell

The remaining minutes contain interview feedback, resume praise and outro promotions.


## Code provenance

The provided source is a **spoken interview transcript**, not a screen recording or extracted source repository. No complete runnable Java files are transcribed. This page preserves only code identifiers explicitly mentioned in the transcript and does not invent code or claim that executable examples were shown.
