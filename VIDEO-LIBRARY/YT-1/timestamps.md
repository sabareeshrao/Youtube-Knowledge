# YT-1 — Mock Interview: Java, Spring Boot, Microservices and System Design

**Source:** [Play this YouTube video](https://www.youtube.com/watch?v=xMlcsFLk-CU) · **58 questions** · **134 timestamp sections**.

Each interview question below is its **own heading and isolated timestamp table**. Every timestamp plays this video only. 🟢 USEFUL · 🟡 INTRO · 🔴 NO NEED.

[See the complete chronological video timeline](timeline.md) · [Original transcript](transcript.md) · [All interview syllabus subjects](../../INTERVIEW-SYLLABUS/README.md)

## Find your interview question

| First timestamp | Interview question |
|---|---|
| [2:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) | [IS-1 — How would you secure a Spring Boot REST API from frontend to backend?](#is-1) |
| [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | [IS-5 — How do access-token expiry and refresh tokens work?](#is-5) |
| [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | [IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?](#is-2) |
| [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | [IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?](#is-3) |
| [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | [IS-4 — What information must not be stored in JWT claims, and why?](#is-4) |
| [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | [IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?](#is-6) |
| [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | [IA-1 — Explain cache-aside caching using Redis and a database.](#ia-1) |
| [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | [IA-2 — How would you control stale cached data using TTL and consistency requirements?](#ia-2) |
| [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | [ID-4 — How do consistency needs differ between cached social content and financial data?](#id-4) |
| [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | [IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.](#is-7) |
| [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | [IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?](#is-8) |
| [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) | [IA-3 — When would you choose GraphQL over REST for an API?](#ia-3) |
| [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | [IA-4 — How does GraphQL field selection compare with REST DTO responses?](#ia-4) |
| [22:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1359s) | [IS-9 — Compare application.properties and application.yml in Spring Boot.](#is-9) |
| [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | [IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.](#ia-5) |
| [25:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1555s) | [IA-6 — How would you gather functional and nonfunctional requirements for an e-commerce platform?](#ia-6) |
| [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | [IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?](#ia-7) |
| [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | [IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.](#ia-8) |
| [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) | [IA-9 — Design product search using a cache, database and search index.](#ia-9) |
| [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | [IA-22 — What tradeoffs affect choosing a database for search versus shopping-cart data?](#ia-22) |
| [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | [ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?](#id-3) |
| [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) | [IA-10 — How would you model a user's cart, and why might you choose a relational database?](#ia-10) |
| [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | [IA-11 — How should cart, product, inventory and user responsibilities be split across services?](#ia-11) |
| [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | [IA-21 — How would backend microservices communicate with each other using HTTP clients?](#ia-21) |
| [41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) | [IA-12 — How do you avoid overselling the last inventory item when Kafka delivery is delayed?](#ia-12) |
| [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) | [IA-13 — How would you implement delivery-partner assignment with asynchronous events?](#ia-13) |
| [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) | [IA-14 — How would you deliver order-status notifications by email and SMS?](#ia-14) |
| [50:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3000s) | [IA-15 — Design an event-driven order-tracking system with a suitable database.](#ia-15) |
| [50:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3038s) | [IA-16 — What data would you collect for logs and commerce analytics?](#ia-16) |
| [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | [ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?](#id-1) |
| [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | [ID-2 — Explain table partitioning versus database sharding.](#id-2) |
| [55:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3359s) | [IA-20 — How would you diagnose Kafka consumer lag in a distributed system?](#ia-20) |
| [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) | [IA-17 — Why use a CDN for an e-commerce product catalog?](#ia-17) |
| [58:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3529s) | [IA-18 — How would you autoscale services when traffic surges during holiday sales?](#ia-18) |
| [59:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3592s) | [IA-19 — How would you implement infinite scroll with pagination, prefetching and loading feedback?](#ia-19) |
| [1:01:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3678s) | [IS-11 — How would you implement backend pagination using Spring Data JPA?](#is-11) |
| [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | [IC-1 — What Git branching and release promotion workflow have you used?](#ic-1) |
| [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | [IC-2 — How do feature branches progress through QA, staging and production?](#ic-2) |
| [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | [IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production?](#is-10) |
| [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | [IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?](#ic-3) |
| [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | [IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.](#ic-4) |
| [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | [IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?](#ic-5) |
| [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | [IC-6 — How would you run and scale ten microservices with Kubernetes?](#ic-6) |
| [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | [IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?](#ic-7) |
| [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | [IC-8 — How would you roll back a broken deployment to a previous container image?](#ic-8) |
| [1:14:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4453s) | [IC-9 — What is infrastructure as code, and how would you use Pulumi for cloud alerts?](#ic-9) |
| [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | [IT-1 — How should a team interpret a claim of 90 to 95 percent unit-test coverage?](#it-1) |
| [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | [IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?](#it-2) |
| [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) | [IT-3 — How is SonarQube used for static analysis and code quality checks?](#it-3) |
| [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | [IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?](#it-4) |
| [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | [IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?](#it-5) |
| [1:22:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4951s) | [IS-12 — What is reactive programming in Spring WebFlux, and how do Mono and Flux differ?](#is-12) |
| [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) | [IC-10 — Compare Maven and Gradle as Java build tools.](#ic-10) |
| [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) | [IC-11 — What is the purpose of pom.xml and how does Maven resolve dependencies?](#ic-11) |
| [1:26:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5212s) | [IC-12 — Compare Kanban and Scrum and explain how they affect a team's delivery workflow.](#ic-12) |
| [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | [IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.](#ij-1) |
| [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | [IJ-3 — How does HashMap fail-fast iteration compare with ConcurrentHashMap iteration?](#ij-3) |
| [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | [IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?](#ij-2) |

## Interview questions and individual timestamp tables

<a id="is-1"></a>

## IS-1 — How would you secure a Spring Boot REST API from frontend to backend?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.4 | [2:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) | 🟢 USEFUL | Spring Security end-to-end question |
| YT-1.5 | [3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) | 🟢 USEFUL | Stateless REST and JWT |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said security should mainly be enforced on the backend, and stateless REST APIs can reuse a JWT sent by the frontend in cookies or a session. He described it as a hash of authentication. | Enforce authentication and authorization at the backend, not merely in the browser. With Spring Security, configure request authorization, validate the access token’s signature, issuer, audience and expiry, and enforce roles/scopes. Use HTTPS, secure token storage and appropriate CSRF/CORS protections. A JWT is not simply an authentication hash. |


<a id="is-5"></a>

## IS-5 — How do access-token expiry and refresh tokens work?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.6 | [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | 🟢 USEFUL | Token expiration and refresh tokens |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He mentioned a short token lifetime and reauthentication after expiry; the interviewer introduced refresh tokens, which he acknowledged without explaining the refresh exchange. | Access tokens expire according to the exp claim. Before or after expiry, an authorized client can exchange a valid refresh token at the authorization server for a new access token; it does not re-send the user’s password on every API call. Protect refresh tokens, use rotation/revocation where supported, and handle expired or stolen tokens safely. |


<a id="is-2"></a>

## IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.7 | [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | 🟢 USEFUL | Okta OAuth authorization server |
| YT-1.8 | [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) | 🟢 USEFUL | Authentication redirect and authorization flow |
| YT-1.9 | [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) | 🟢 USEFUL | Callback URLs and identity-provider configuration |
| YT-1.10 | [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) | 🟢 USEFUL | Frontend-to-Okta-to-backend flow |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described using Okta with Spring Security, an Okta sign-in page, configured callback URLs, and tokens forwarded from the frontend to the API. He loosely referred to API/access keys for configuration. | Use OpenID Connect/OAuth 2.0 authorization-code flow, typically with PKCE for a browser client. Redirect to Okta, receive an authorization code at a registered redirect URI, exchange it securely for tokens, then have Spring Security validate access tokens. Configure issuer, client credentials where applicable, audience, scopes and role mapping; do not put confidential client secrets in browser code. |


<a id="is-3"></a>

## IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.11 | [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | 🟢 USEFUL | How a backend validates JWTs |
| YT-1.12 | [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) | 🟢 USEFUL | JWT signature and payload discussion — JWT payload is encoded, not automatically encrypted |
| YT-1.13 | [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) | 🟢 USEFUL | Questionable JWT validation explanation — WARNING: candidate's token-validation claim is incorrect; validate signature and claims |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said a JWT has three parts and a signature that reveals tampering, but suggested decoding or hashing it back and comparing a password or user ID against the database to trust the caller. | JWT verification is not reverse hashing. A resource server validates a trusted signature (or MAC), expected algorithm, issuer, audience, expiration/not-before and relevant authorization claims. Spring Security OAuth2 Resource Server can validate JWTs using an issuer/JWK set. Never place passwords inside JWT payloads or trust a token just because its decoded fields match a database record. |


<a id="is-4"></a>

## IS-4 — What information must not be stored in JWT claims, and why?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.14 | [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | 🟢 USEFUL | Sensitive data inside JWT claims |
| YT-1.15 | [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) | 🟢 USEFUL | Password and JWT payload safety |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He initially argued that JWT hashing prevented outsiders from recovering sensitive information, but later agreed that passwords and personal details should not be placed in the token body. | A common signed JWT is base64url-encoded, not encrypted: anyone holding it can read header and payload. Never put passwords, credential hashes, access secrets or unnecessary personal data in its claims. Signatures protect integrity, not confidentiality; use TLS, minimal claims, and encryption only when separately required. |


<a id="is-6"></a>

## IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.17 | [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | 🟢 USEFUL | Duplicate scheduled jobs across replicas |
| YT-1.18 | [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) | 🟢 USEFUL | ShedLock for single scheduler execution |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He correctly noted that @Scheduled runs independently in each application replica and proposed ShedLock to prevent three instances from writing the same record. | A local Spring scheduler does not coordinate replicas. Use a shared distributed lock such as ShedLock with a properly configured persistent lock provider, or a dedicated scheduler/queue with leader election. Set lock durations carefully and still make the job idempotent, because retries and crashes can otherwise cause duplicates. |


<a id="ia-1"></a>

## IA-1 — Explain cache-aside caching using Redis and a database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.19 | [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | 🟡 INTRO | Caching discussion begins |
| YT-1.20 | [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) | 🟢 USEFUL | Redis cache-aside lookup |
| YT-1.21 | [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) | 🟢 USEFUL | In-memory caching and latency |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described Redis as an in-memory key-value cache checked before querying the database, reducing latency for frequently read data. | That is cache-aside: read cache, on miss read authoritative storage, write the result to cache with appropriate TTL, and return it. Redis is a separate shared in-memory service, not necessarily local RAM inside each app instance. Plan invalidation, miss storms, serialization and failure fallback. |


<a id="ia-2"></a>

## IA-2 — How would you control stale cached data using TTL and consistency requirements?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.22 | [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | 🟢 USEFUL | Cache TTL and freshness |
| YT-1.23 | [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) | 🟢 USEFUL | Stale cached data and TTL tradeoffs |
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described TTL-based caching, recognized possible stale results, and said eventual consistency can be acceptable for some apps but not financial balances. He did not give a concrete invalidation design. | Choose freshness guarantees by business use case. On writes, invalidate or update affected cache keys; complement this with TTL, versioning/events and retryable invalidation. TTL alone bounds staleness imperfectly and short TTLs increase load. Describe race conditions, read-after-write needs and strong-consistency paths for critical values. |


<a id="id-4"></a>

## ID-4 — How do consistency needs differ between cached social content and financial data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said stale reads may be acceptable for social feeds but account balances must not show inaccurate values across users. | Define required consistency for each operation. Feeds and recommendation caches may tolerate bounded staleness, while available balances and payment authorization should read from an authoritative consistent source or use transactional safeguards. Invalidate related caches on writes and document read-after-write requirements and acceptable delay. |


<a id="is-7"></a>

## IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He associated Hibernate L1 with an individual Session and L2 with SessionFactory, saying L1 is enabled by default and L2 can share entities across sessions. | Hibernate’s first-level cache (persistence context) is mandatory and scoped to a Session/EntityManager. The optional second-level cache is managed at SessionFactory scope through a configured cache provider and caching policies. L2 is not a magical cache of every entity; explain regions, invalidation, transaction consistency and when it is appropriate. |


<a id="is-8"></a>

## IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.31 | [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | 🟢 USEFUL | Why SessionFactory is expensive and shared |
| YT-1.32 | [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) | 🟢 USEFUL | Multiple databases and SessionFactory instances |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said SessionFactory is expensive, should be reused as a singleton, and different databases generally need separate SessionFactory instances. He also compared one SessionFactory to one database connection. | SessionFactory is expensive to build but thread-safe and reused, typically one per persistence unit/configuration. It creates many short-lived Sessions and works with a connection pool; it is not one database connection. With multiple independently configured databases/persistence units, configure corresponding factories/entity managers and transaction boundaries. |


<a id="ia-3"></a>

## IA-3 — When would you choose GraphQL over REST for an API?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.33 | [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) | 🟢 USEFUL | Why GraphQL instead of REST |
| YT-1.34 | [19:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1145s) | 🟢 USEFUL | GraphQL query entry point |
| YT-1.35 | [19:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1169s) | 🟢 USEFUL | GraphQL versus REST decision criteria |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He preferred GraphQL when a REST design requires many endpoints and said GraphQL can service several entity requirements through a common endpoint. | Choose GraphQL when clients need flexible shapes, related data and self-described schema-driven queries; use REST when simple resources, HTTP caching and operational simplicity fit better. GraphQL is not automatically faster or always one endpoint. Address N+1 queries, query complexity limits, authorization at field/resolver level and caching. |


<a id="ia-4"></a>

## IA-4 — How does GraphQL field selection compare with REST DTO responses?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.36 | [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | 🟢 USEFUL | GraphQL field-level selection |
| YT-1.37 | [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) | 🟢 USEFUL | REST DTO and field filtering alternatives |
| YT-1.38 | [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) | 🟢 USEFUL | Variable response fields across clients |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He argued REST can reduce response fields via DTOs or @JsonIgnore, while GraphQL lets each caller select requested fields more conveniently. | GraphQL clients specify selected fields at query time. REST can also provide sparse fieldsets, projections, query parameters or alternate DTOs without always changing source code. @JsonIgnore is mostly static serialization exclusion, not the same as per-request selection. Compare schema governance, authorization, overfetching and resolver performance. |


<a id="is-9"></a>

## IS-9 — Compare application.properties and application.yml in Spring Boot.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.39 | [22:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1359s) | 🟢 USEFUL | External Spring Boot configuration |
| YT-1.40 | [23:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1380s) | 🟢 USEFUL | Properties versus YAML |
| YT-1.41 | [23:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1418s) | 🟢 USEFUL | Hierarchical YAML configuration |
| YT-1.42 | [24:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1453s) | 🟢 USEFUL | Structured configuration values |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He explained that properties repeat dotted prefixes while YAML nests values hierarchically and supports lists/maps. He treated the difference as mostly readability and expanded YAML’s acronym incorrectly. | Spring Boot can bind both .properties and .yml to the same configuration properties. YAML is useful for nested maps/lists; properties are simple and explicit. YAML stands for “YAML Ain’t Markup Language.” Consider profile overrides, config source precedence, validation and secret management rather than declaring one universally superior. |


<a id="ia-5"></a>

## IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.43 | [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | 🟢 USEFUL | Distributed transactions in microservices |
| YT-1.44 | [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) | 🟢 USEFUL | Saga versus two-phase commit |
| YT-1.45 | [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) | 🟢 USEFUL | Saga events and compensating actions |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He contrasted Saga’s event-triggered local transactions and compensating operations with synchronous two-phase commit, but at times spoke as if Saga could provide one atomic end-to-end transaction. | Saga coordinates independently committed local transactions through orchestration or choreography and compensating actions after failure; it does not provide global ACID atomicity or instant rollback. Two-phase commit coordinates participants for atomic commit but adds blocking, availability and operational costs. Choose based on consistency requirements, failure recovery and service autonomy. |


<a id="ia-6"></a>

## IA-6 — How would you gather functional and nonfunctional requirements for an e-commerce platform?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.46 | [25:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1555s) | 🟡 INTRO | E-commerce system-design prompt |
| YT-1.47 | [26:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1618s) | 🟢 USEFUL | Functional e-commerce requirements |
| YT-1.48 | [27:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1655s) | 🟢 USEFUL | Nonfunctional requirements |
| YT-1.49 | [28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1717s) | 🟢 USEFUL | Search, cart, order, delivery and notification scope |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He listed product browsing/search, cart, payment, delivery and notifications as functional requirements, and scale, resilience and latency as nonfunctional concerns. | Start with explicit user flows, inventory/payment correctness, failure paths and measurable nonfunctional targets: peak QPS, latency SLO, availability, data consistency, security and recovery objectives. Clarify constraints and workload assumptions before choosing databases or services, and prioritize core flows before optional features. |


<a id="ia-7"></a>

## IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.50 | [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | 🟢 USEFUL | Abusive traffic and peak sale load |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.54 | [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) | 🟢 USEFUL | Rate limiting suspicious requests |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed a proxy/load balancer and request limits, including watching repeated calls from an IP, to stop abusive traffic. | Apply rate limiting at an API gateway/edge using token bucket or sliding-window policies per identity, token, endpoint and IP, backed by a shared limiter when necessary. Add WAF/bot controls, authentication, quotas and observability. IP-only throttling can punish shared networks; tune legitimate burst allowances and abuse responses. |


<a id="ia-8"></a>

## IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.51 | [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | 🟢 USEFUL | Client and web/mobile system entry point |
| YT-1.52 | [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) | 🟢 USEFUL | Load balancers for replicated services |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.55 | [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) | 🟢 USEFUL | Search service and microservice boundary |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He drew clients feeding an Nginx-like reverse proxy/load balancer, which routes requests to replicated microservices. | A solid overview includes clients, CDN/WAF, gateway or reverse proxy, load-balanced stateless services, authentication, service discovery, databases, caching, messaging and observability. Define service ownership and request flow, scaling/failure modes and consistency, not just the drawing. Add health checks, retries with limits and graceful degradation. |


<a id="ia-9"></a>

## IA-9 — Design product search using a cache, database and search index.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.56 | [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) | 🟢 USEFUL | Redis cache for product search |
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.58 | [36:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2165s) | 🟢 USEFUL | Elasticsearch for product queries |
| YT-1.59 | [37:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2259s) | 🟢 USEFUL | Text search and typo-tolerant indexing |
| YT-1.60 | [38:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2297s) | 🟢 USEFUL | Hot search queries cached in Redis |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He combined product search with Redis caching, Cassandra/MongoDB as product storage and Elasticsearch for keyword/typo search, assuming search can tolerate some staleness. | Keep authoritative product/catalog data in a suitable operational store, maintain a dedicated search index asynchronously via a reliable change pipeline, and cache hot queries in Redis with expiration/invalidation. Use an Elasticsearch/OpenSearch query service for text relevance. Protect inventory/pricing correctness at checkout; search-index and cache consistency need explicit update/rebuild plans. |


<a id="ia-22"></a>

## IA-22 — What tradeoffs affect choosing a database for search versus shopping-cart data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He leaned toward NoSQL for varied product/search schemas and MySQL for structured cart relations and consistency. | Choose storage from query patterns and invariants, not simply “structured versus unstructured.” Search often benefits from a specialized index, catalogs may use SQL or document stores, and orders/inventory need strong transactional guarantees. Compare transactions, indexing, scaling, failure recovery and consistency explicitly. |


<a id="id-3"></a>

## ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He selected Cassandra/MongoDB for search-related product data and SQL for cart relationships; for shipment tracking he revised an initial NoSQL decision to SQL. | For product catalog, choose SQL/document storage from update and query needs; maintain a search index separately for text queries. Use relational transactions where cart/order/stock invariants require them. Tracking is often an append-only relational event table. Operational simplicity and access patterns matter more than a rule that every microservice needs NoSQL. |


<a id="ia-10"></a>

## IA-10 — How would you model a user's cart, and why might you choose a relational database?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.61 | [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) | 🟢 USEFUL | Cart service data model |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He modeled cart items as a one-to-many user association and chose MySQL for structured relations and consistency, loosely invoking the CAP theorem. | Model cart, cart_line_item and product references with stable IDs, quantities and constraints. A relational database supports joins and transactions, but CAP is not a direct rule saying “use MySQL for cart.” Plan concurrent cart updates, optimistic locking/versioning, expiration and price/stock revalidation at checkout. |


<a id="ia-11"></a>

## IA-11 — How should cart, product, inventory and user responsibilities be split across services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |
| YT-1.68 | [43:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2638s) | 🟢 USEFUL | Inventory and product service split |
| YT-1.69 | [44:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2683s) | 🟢 USEFUL | Single responsibility for product service |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed distinct cart, product, inventory and user services and REST/Feign-style communication to preserve one responsibility per service. | Split services by clear business ownership: catalog/product, inventory availability/reservation, cart, order, payment and identity. Define owned databases, API/event contracts, idempotent interactions and failure boundaries. “One service per noun” is not automatically best; use cohesive bounded contexts and avoid synchronous call chains across every operation. |


<a id="ia-21"></a>

## IA-21 — How would backend microservices communicate with each other using HTTP clients?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said microservices exchange data through REST calls using RestTemplate or Feign, without going into client reliability. | For synchronous HTTP use an appropriate typed client such as Spring RestClient, WebClient or OpenFeign. Define contracts, connection and request timeouts, retry policies only for safe/idempotent calls, circuit breakers, authentication and tracing. Use asynchronous messaging where workflows should not wait on another service. |


<a id="ia-12"></a>

## IA-12 — How do you avoid overselling the last inventory item when Kafka delivery is delayed?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.64 | [41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) | 🟢 USEFUL | Order and delivery business workflow |
| YT-1.65 | [42:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2521s) | 🟢 USEFUL | Kafka events and inventory reduction |
| YT-1.66 | [42:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2561s) | 🟢 USEFUL | Overselling due to delayed consumers |
| YT-1.67 | [43:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2599s) | 🟢 USEFUL | Inventory consistency reconsidered |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He initially proposed Kafka events to reduce stock after an order; when challenged about two customers buying the last item before consumers catch up, he admitted the race and suggested synchronous handling. | Do not rely on delayed Kafka consumers to guarantee stock availability. Atomically reserve/decrement inventory within the inventory store using a conditional update or serializable/locking strategy before confirming the order. Then publish reliable events via an outbox for notifications and downstream workflows. Handle idempotency, reservation expiry and compensation on payment failure. |


<a id="ia-13"></a>

## IA-13 — How would you implement delivery-partner assignment with asynchronous events?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.70 | [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) | 🟢 USEFUL | Assigning delivery partners |
| YT-1.71 | [46:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2765s) | 🟢 USEFUL | Structured delivery partner storage |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |
| YT-1.73 | [48:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2896s) | 🟢 USEFUL | Delivery assignment need not be immediate |
| YT-1.74 | [48:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2930s) | 🟢 USEFUL | Kafka event-driven delivery processing |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He designed a SQL-backed delivery-partner service; after discussion, he agreed assignment can occur after the order and be driven asynchronously through Kafka. | Make delivery assignment an asynchronous post-order workflow: publish an OrderReadyForDispatch event reliably, match eligible partners and persist assignment transactionally. Consumers must be idempotent and retry safely; track unassigned orders, timeout and reassignment. Payment and inventory guarantees should be handled before dispatch eligibility. |


<a id="ia-14"></a>

## IA-14 — How would you deliver order-status notifications by email and SMS?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.75 | [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) | 🟢 USEFUL | Email and SMS notifications |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed a notification service consuming Kafka events and choosing email or SMS based on each customer’s preference. | Consume domain events in a dedicated notification service, render templates and honor channel preferences and consent. Use idempotency keys to prevent duplicate sends, provider retries/backoff, dead-letter queues and delivery-status tracking. Never block the core order transaction on an external email/SMS provider. |


<a id="ia-15"></a>

## IA-15 — Design an event-driven order-tracking system with a suitable database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.76 | [50:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3000s) | 🟢 USEFUL | Order tracking requirement |
| YT-1.78 | [51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) | 🟢 USEFUL | Tracking events through Kafka |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |
| YT-1.80 | [53:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3195s) | 🟢 USEFUL | Delivery confirmation asynchronously |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He suggested Kafka-driven tracking updates with status timestamps, initially chose NoSQL, then accepted that structured SQL records could fit tracking better. | Store append-only shipment/status events with order ID, carrier/partner, timestamp and state; derive the current shipment status for reads. A relational table often fits this schema well, though event stores/NoSQL may be justified by scale. Consume events idempotently, deduplicate and handle out-of-order arrivals explicitly. |


<a id="ia-16"></a>

## IA-16 — What data would you collect for logs and commerce analytics?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.77 | [50:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3038s) | 🟢 USEFUL | Logs and sales analytics |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed storing logs, possibly in S3, and analyzing sales trends with a tool such as Spark to improve stock or promotions. | Separate operational observability (structured logs, metrics, traces, correlation IDs, error rates) from business analytics (orders, conversion, search, returns). Stream events into governed storage/warehouse with retention, privacy and data-quality controls. Analytics jobs can inform forecasting, but logging should not expose customer secrets. |


<a id="id-1"></a>

## ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.81 | [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | 🟢 USEFUL | Slow SQL query diagnosis |
| YT-1.82 | [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) | 🟢 USEFUL | Indexing and query profiling |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He suggested first profiling the slow query and checking indexes, then partitioning large datasets if the table itself is a bottleneck. | Capture the slow SQL and use EXPLAIN/EXPLAIN ANALYZE plus query and database metrics. Check missing/poor indexes, selectivity, join plans, row counts, locking, statistics, overfetching and N+1 access. Benchmark changes and account for index write costs before trying partitioning, caching or sharding. |


<a id="id-2"></a>

## ID-2 — Explain table partitioning versus database sharding.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.83 | [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | 🟢 USEFUL | Database partitioning |
| YT-1.84 | [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) | 🟢 USEFUL | Sharding versus partitioning |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He distinguished partitioning as splitting data within one server and sharding as distributing portions of the dataset across different servers or locations. | Partitioning divides a table logically or physically by a key, often within one database instance, improving pruning and maintenance when queries align. Sharding distributes ownership of data across independent database instances/nodes. Both can span physical machines depending on implementation; explain shard keys, routing, cross-shard queries and rebalancing. |


<a id="ia-20"></a>

## IA-20 — How would you diagnose Kafka consumer lag in a distributed system?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.85 | [55:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3359s) | 🟢 USEFUL | Kafka consumer lag interview question — no clear tested remedy demonstrated |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He interpreted Kafka lag as a broker resilience/leader–follower issue rather than a backlog of unprocessed messages; the transcript does not demonstrate a specific consumer-lag fix. | Consumer lag is the difference between produced offsets and consumer-group committed/processed offsets. Inspect lag per partition, throughput, consumer errors, rebalances, processing latency and downstream dependencies. Tune batch sizes or processing, add consumers up to partition count, raise partitions carefully and apply backpressure; monitor progress rather than confusing lag with broker replication. |


<a id="ia-17"></a>

## IA-17 — Why use a CDN for an e-commerce product catalog?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.86 | [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) | 🟢 USEFUL | CDN for images and static content |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said product images and other static files could be copied to geographically distributed CDN locations, giving customers nearby delivery. | A CDN caches eligible static assets at edge locations, reducing origin requests and latency. Set cache-control and TTL, version asset URLs, compress/resize images and secure origin access. Product availability, user-specific details and private data usually require different caching policies. |


<a id="ia-18"></a>

## IA-18 — How would you autoscale services when traffic surges during holiday sales?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.87 | [58:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3529s) | 🟢 USEFUL | Autoscaling during sales spikes |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described cloud monitoring that scales instance counts up when CPU crosses a threshold and down when demand falls. | Configure horizontal autoscaling against CPU, request rate, queue depth or suitable custom metrics, with safe minimum/maximum replicas and cooldown behavior. Add readiness probes, load tests and capacity limits; scaling services alone does not solve database bottlenecks or cold starts. Define SLOs and monitor cost versus latency. |


<a id="ia-19"></a>

## IA-19 — How would you implement infinite scroll with pagination, prefetching and loading feedback?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.88 | [59:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3592s) | 🟢 USEFUL | Backend and frontend pagination prompt |
| YT-1.89 | [1:00:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3628s) | 🟢 USEFUL | Lazy loading and infinite scrolling |
| YT-1.91 | [1:01:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3719s) | 🟢 USEFUL | Latency between scrolling and API response |
| YT-1.92 | [1:02:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3761s) | 🟢 USEFUL | Prefetching before viewport end |
| YT-1.93 | [1:03:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3786s) | 🟢 USEFUL | Skeleton states, debounce and throttle |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed loading initial product batches, fetching more during infinite scrolling, then prefetching before the bottom and showing loading indicators to hide latency. | Use stable cursor/keyset or correctly ordered page-based endpoints, request the next window ahead of viewport intersection and deduplicate responses. Show skeleton/placeholder states, handle errors and avoid overlapping fetches. Throttle/debounce scroll input when relevant, but distinguish event control from backend pagination. |


<a id="is-11"></a>

## IS-11 — How would you implement backend pagination using Spring Data JPA?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.90 | [1:01:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3678s) | 🟢 USEFUL | JPA pagination and batch fetching |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described loading bounded batches and a next-page number/size through JPA or EntityManager, but admitted he was unsure of the exact query/API. | In Spring Data JPA use a repository method accepting Pageable, e.g. PageRequest.of(page, size, Sort.by(...)), returning Page or Slice. Always use deterministic sorting, bound page sizes and understand count-query cost. For very deep pagination consider keyset/cursor pagination; avoid confusing JDBC batch updates with paginated reads. |


<a id="ic-1"></a>

## IC-1 — What Git branching and release promotion workflow have you used?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described feature branches, dev/QA stages, a preproduction branch and a stable production branch with testing between promotions. | Use protected main/release branches or trunk-based development with short-lived feature branches, PR review and automated build/security/test gates. Promote a versioned, tested artifact through environments rather than rebuilding different code. Explain tagging, releases, rollback and how hotfixes flow back to main. |


<a id="ic-2"></a>

## IC-2 — How do feature branches progress through QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described development branches progressing through QA and preproduction before stable production, with different environment settings. | Treat environments as deployment targets, not necessarily one Git branch each. Build once and promote immutable artifacts through test, staging and production with approvals and environment-specific secrets/configuration. Use protected branches and clear release ownership to prevent drift. |


<a id="is-10"></a>

## IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.97 | [1:05:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3946s) | 🟢 USEFUL | Spring profiles with per-environment properties |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said Spring Boot uses application.properties by default and can load application-dev, QA, staging or production files to override environment-specific database/settings. | Activate profiles using SPRING_PROFILES_ACTIVE, --spring.profiles.active or another supported configuration source. Spring Boot loads profile-specific application-{profile}.properties or YAML, subject to property-source precedence. Deploy the same tested artifact to environments; inject credentials through managed secrets or environment configuration, not committed passwords. |


<a id="ic-3"></a>

## IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said GitHub Actions or Jenkins notices a new commit/merge, runs tests and automatically deploys, suggesting it periodically checks changed commit IDs. | A PR merge normally triggers a push/webhook or CI workflow event; it need not rely on periodic commit polling. The pipeline checks out an immutable commit, builds, runs tests/scans, publishes a versioned artifact and deploys under approval/health gates. Distinguish CI triggers, artifact promotion and production-release policy. |


<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |
| YT-1.100 | [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) | 🟢 USEFUL | Continuous integration checks |
| YT-1.101 | [1:08:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4122s) | 🟢 USEFUL | Continuous delivery and deployment |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said CI automates integration and test execution on commits, while CD moves verified changes toward deployment after passing tests. | CI continuously merges/checks changes with builds, unit/integration tests and quality gates. Continuous delivery keeps releasable artifacts ready but may require production approval; continuous deployment automatically releases every change that passes gates. Include secure artifact publishing, rollback and environment-specific deployment verification. |


<a id="ic-5"></a>

## IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.102 | [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | 🟢 USEFUL | Dockerfile, image and container |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described a Dockerfile with JDK version, application startup entry point, exposed ports and dependencies that run a Java JAR. | A Dockerfile describes an image build: select a suitable base runtime (up to Java 21 here), copy the built JAR, configure a non-root user and ENTRYPOINT, and optionally document EXPOSE. Images are immutable packages; containers are running instances. Inject secrets and environment config at runtime and scan/minimize image layers. |


<a id="ic-6"></a>

## IC-6 — How would you run and scale ten microservices with Kubernetes?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.103 | [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | 🟢 USEFUL | Managing multiple microservice containers |
| YT-1.104 | [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) | 🟢 USEFUL | Kubernetes orchestration and replicas |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He suggested Kubernetes orchestrates containers, adds/removes replicas based on load and runs packaged microservice images in production. | Push immutable images to a container registry, deploy each workload via Kubernetes Deployment/Service resources, and configure health probes, resource requests/limits and autoscaling (HPA where appropriate). Kubernetes reconciles desired state but you must configure autoscaling policies, rollout strategy, networking and observability. |


<a id="ic-7"></a>

## IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.105 | [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | 🟢 USEFUL | Repeated Kubernetes pod crashes and CrashLoopBackOff scenario |
| YT-1.106 | [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) | 🟢 USEFUL | Crash triage, logs and PagerDuty |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He mentioned PagerDuty alerts and manual intervention when a pod repeatedly restarts; he said he had not implemented an additional automation solution. | For CrashLoopBackOff inspect kubectl describe pod, events, logs --previous, exit codes/OOMKilled, configuration, secrets, dependencies and probes. Compare rollout changes, mitigate via rollback or corrected config, and monitor recovery. PagerDuty routes an incident; it is not the technical fix. |


<a id="ic-8"></a>

## IC-8 — How would you roll back a broken deployment to a previous container image?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.107 | [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | 🟢 USEFUL | Rollback to previous application version |
| YT-1.108 | [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) | 🟢 USEFUL | Release versioning and rollback workflow |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said Docker images have versions and Kubernetes can go back to a previous version when the newest one fails, but the actual rollback mechanics were vague. | Tag/digest images immutably, use rollout history and a controlled rollback such as kubectl rollout undo deployment/name or redeploy a known-good image. Kubernetes does not automatically roll back every failed Deployment by default. Verify readiness, error rates and dependencies after rollback. |


<a id="ic-9"></a>

## IC-9 — What is infrastructure as code, and how would you use Pulumi for cloud alerts?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.109 | [1:14:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4453s) | 🟢 USEFUL | Infrastructure as code with Pulumi |
| YT-1.110 | [1:14:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4481s) | 🟢 USEFUL | Azure alerting and infrastructure automation |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described Pulumi as Terraform-like infrastructure automation, reported Azure authentication/alert work, but suggested Pulumi is mainly YAML configuration without real coding. | Pulumi is infrastructure as code using TypeScript/JavaScript, Python, Go, C#, Java or YAML. Define resources and alerts in version-controlled projects, manage encrypted configuration/state and preview/apply changes through CI. Explain alert rules, thresholds, notification targets, permissions and drift/rollback management. |


<a id="it-1"></a>

## IT-1 — How should a team interpret a claim of 90 to 95 percent unit-test coverage?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.111 | [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | 🟢 USEFUL | High test coverage question |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said he tests methods using JUnit 5 and mocks, and uses coverage/static analysis tools. He did not clearly justify which statements or behaviors count toward 90–95 percent coverage. | Coverage is a signal, not a target that proves correctness. Prioritize business branches, boundary cases, failures and contract behavior; inspect line/branch coverage and mutation testing when useful. Explain justified exclusions and quality gates, while avoiding trivial tests written solely to raise a percentage. |


<a id="it-2"></a>

## IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.112 | [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | 🟢 USEFUL | JUnit tests and mocked dependencies |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said JUnit 5 tests cover individual methods and mocks stand in for database calls or other external dependencies. | Use JUnit 5 plus Mockito to inject mocked repositories/clients, arrange behavior, call the service and assert outputs and important interactions. Test edge/error cases without real external services in unit tests. Use separate integration tests with realistic dependencies for persistence and wire behavior. |


<a id="it-3"></a>

## IT-3 — How is SonarQube used for static analysis and code quality checks?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.113 | [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) | 🟢 USEFUL | SonarQube and static analysis |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said he used SonarQube for code/static analysis and configured its server URL/properties, but his described integration was mainly from an Android project. | SonarQube analyzes source against code-quality/security rules and quality gates; feed it coverage reports such as JaCoCo output through the scanner/CI pipeline. Configure project identity, authentication, analysis path and branch/PR checks. It complements, rather than replaces, unit and integration tests. |


<a id="it-4"></a>

## IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.114 | [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | 🟢 USEFUL | Do not test trivial getters just for coverage |
| YT-1.115 | [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) | 🟢 USEFUL | Exclude DTO boilerplate from coverage |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He agreed that testing every DTO getter/setter is low value and said Maven XML exclusion patterns can omit boilerplate packages from coverage reporting. | Test behavior and meaningful serialization/validation contracts, not trivial accessors for percentages. Configure JaCoCo report exclusions or coverage rules explicitly, document why generated/DTO code is omitted, and do not use blanket exclusions to conceal untested logic. |


<a id="it-5"></a>

## IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.116 | [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | 🟢 USEFUL | Integration tests for entities and services |
| YT-1.117 | [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) | 🟢 USEFUL | Microservice end-to-end testing |
| YT-1.118 | [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) | 🟢 USEFUL | Avoid real cross-service calls in unit tests |
| YT-1.119 | [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) | 🟢 USEFUL | Use separate integration/system-test suites |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described calling actual REST endpoints across microservices in tests and checking responses, then agreed those calls should be separated from fast unit tests. | Unit tests mock remote clients and run quickly. Integration tests check adapters and real dependencies (often via Testcontainers or stubbed services); contract tests validate provider/consumer interfaces. A small end-to-end suite exercises deployed service flows. Separate suites by CI stage to avoid flaky, slow unit builds. |


<a id="is-12"></a>

## IS-12 — What is reactive programming in Spring WebFlux, and how do Mono and Flux differ?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.120 | [1:22:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4951s) | 🟡 INTRO | Introduction to reactive Spring applications |
| YT-1.121 | [1:22:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4966s) | 🟢 USEFUL | Blocking versus nonblocking I/O |
| YT-1.122 | [1:23:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5013s) | 🟢 USEFUL | Mono and Flux overview |
| YT-1.123 | [1:23:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5032s) | 🟢 USEFUL | Project Reactor in Spring |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He contrasted waiting threads with callback-like, nonblocking operations and mentioned Reactor’s Mono and Flux for small versus multiple results. | Spring WebFlux uses Reactive Streams publishers: Mono emits zero or one item, Flux emits zero to many. Nonblocking I/O helps high-concurrency I/O-bound workloads but does not make CPU work faster. Avoid blocking calls on event-loop threads, handle backpressure/errors and select the model based on dependencies and workload. |


<a id="ic-10"></a>

## IC-10 — Compare Maven and Gradle as Java build tools.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.124 | [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) | 🟢 USEFUL | Maven versus Gradle question |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He called Maven and Gradle build tools, associated Maven with pom.xml and said Gradle may feel faster although either can build the same project. | Maven uses a declarative XML POM and standard lifecycle; Gradle supports Groovy/Kotlin DSL and incremental/cached builds. Both resolve dependencies, execute plugins/tasks and produce artifacts. Compare team conventions, build reproducibility, cacheability and measured performance—not blanket speed claims. |


<a id="ic-11"></a>

## IC-11 — What is the purpose of pom.xml and how does Maven resolve dependencies?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.125 | [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) | 🟢 USEFUL | Interview question switches to why pom.xml is used |
| YT-1.126 | [1:25:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5136s) | 🟢 USEFUL | Purpose of pom.xml |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said a POM declares required JARs and versions, letting Maven look locally first and then download missing artifacts instead of manually sharing library files. | pom.xml defines project coordinates, dependencies, repositories, plugins and build lifecycle configuration. Maven resolves transitive dependencies through configured repositories, caching them locally; dependencyManagement controls versions. Explain reproducible builds, plugin goals and why secrets/absolute machine paths should not be embedded. |


<a id="ic-12"></a>

## IC-12 — Compare Kanban and Scrum and explain how they affect a team's delivery workflow.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.127 | [1:26:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5212s) | 🟢 USEFUL | Kanban versus Scrum in team workflow |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He understood Kanban as adaptive Agile project management and admitted he had not worked on a fully Kanban-based team, only a mix with Scrum. | Scrum organizes work into timeboxed sprints with defined accountabilities/events; Kanban optimizes continuous flow with a visual board, pull policies and work-in-progress limits. Teams can combine practices. Be explicit about personal experience and discuss lead/cycle time, bottlenecks and predictable delivery. |


<a id="ij-1"></a>

## IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.128 | [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | 🟢 USEFUL | ConcurrentHashMap internal design question |
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |
| YT-1.131 | [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) | 🟢 USEFUL | Legacy segment-lock explanation caveat |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said HashMap iterators can fail when entries change during iteration, while ConcurrentHashMap handles concurrent writes without that iterator exception. He described an older segmented-locking model. | HashMap is not thread-safe; fail-fast iteration is best-effort and does not make access safe. ConcurrentHashMap supports safe concurrent operations and weakly consistent iterators; modern implementations use fine-grained synchronization/CAS, not a fixed simple set of 16 segment locks. Use atomic APIs such as computeIfAbsent when coordination is needed. |


<a id="ij-3"></a>

## IJ-3 — How does HashMap fail-fast iteration compare with ConcurrentHashMap iteration?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He contrasted HashMap's iterator exception on structural changes with ConcurrentHashMap supporting changes during iteration, but named the exception imprecisely. | HashMap iterators may throw ConcurrentModificationException on structural modification (fail-fast is best-effort, not a safety guarantee). ConcurrentHashMap iterators are weakly consistent: they neither throw that exception for concurrent updates nor promise a single atomic snapshot. Choose based on access and iteration-consistency requirements. |


<a id="ij-2"></a>

## IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.132 | [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | 🟢 USEFUL | Using employee objects as HashMap keys |
| YT-1.133 | [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) | 🟢 USEFUL | equals and hashCode contract |

### Candidate answer vs. AI-corrected answer — YT-1

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said a custom Employee key should override equals() and hashCode() to distinguish logically equal keys and avoid duplicate entries. | Implement equals() and hashCode() consistently: equal objects must produce equal hash codes, and key fields should remain stable while stored. HashMap uses hash buckets and equality comparisons on collisions/matches. Prefer immutable identifiers/keys, and test equal, unequal and collision scenarios. |


## Which additional introductions or transitions can be skipped?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.1 | [0:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=0s) | 🔴 NO NEED | Opening promotions and channel announcements |
| YT-1.2 | [1:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=90s) | 🟡 INTRO | Candidate introduction |
| YT-1.3 | [2:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=120s) | 🟡 INTRO | Experience and technology stack |
| YT-1.16 | [10:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=614s) | 🟡 INTRO | Transition from security to scheduling |
| YT-1.26 | [14:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=886s) | 🟡 INTRO | Transition to Hibernate caching |
| YT-1.94 | [1:03:51](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3831s) | 🟡 INTRO | Transition to Git branching and delivery |
| YT-1.134 | [1:32:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5532s) | 🔴 NO NEED | Interview feedback and farewell |

*Questions are curated from the video discussion, not necessarily verbatim interviewer wording.*
