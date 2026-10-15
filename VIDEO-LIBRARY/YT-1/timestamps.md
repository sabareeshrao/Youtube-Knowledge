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

<a id="is-5"></a>

## IS-5 — How do access-token expiry and refresh tokens work?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.6 | [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | 🟢 USEFUL | Token expiration and refresh tokens |

<a id="is-2"></a>

## IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.7 | [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | 🟢 USEFUL | Okta OAuth authorization server |
| YT-1.8 | [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) | 🟢 USEFUL | Authentication redirect and authorization flow |
| YT-1.9 | [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) | 🟢 USEFUL | Callback URLs and identity-provider configuration |
| YT-1.10 | [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) | 🟢 USEFUL | Frontend-to-Okta-to-backend flow |

<a id="is-3"></a>

## IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.11 | [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | 🟢 USEFUL | How a backend validates JWTs |
| YT-1.12 | [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) | 🟢 USEFUL | JWT signature and payload discussion — JWT payload is encoded, not automatically encrypted |
| YT-1.13 | [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) | 🟢 USEFUL | Questionable JWT validation explanation — WARNING: candidate's token-validation claim is incorrect; validate signature and claims |

<a id="is-4"></a>

## IS-4 — What information must not be stored in JWT claims, and why?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.14 | [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | 🟢 USEFUL | Sensitive data inside JWT claims |
| YT-1.15 | [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) | 🟢 USEFUL | Password and JWT payload safety |

<a id="is-6"></a>

## IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.17 | [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | 🟢 USEFUL | Duplicate scheduled jobs across replicas |
| YT-1.18 | [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) | 🟢 USEFUL | ShedLock for single scheduler execution |

<a id="ia-1"></a>

## IA-1 — Explain cache-aside caching using Redis and a database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.19 | [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | 🟡 INTRO | Caching discussion begins |
| YT-1.20 | [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) | 🟢 USEFUL | Redis cache-aside lookup |
| YT-1.21 | [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) | 🟢 USEFUL | In-memory caching and latency |

<a id="ia-2"></a>

## IA-2 — How would you control stale cached data using TTL and consistency requirements?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.22 | [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | 🟢 USEFUL | Cache TTL and freshness |
| YT-1.23 | [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) | 🟢 USEFUL | Stale cached data and TTL tradeoffs |
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

<a id="id-4"></a>

## ID-4 — How do consistency needs differ between cached social content and financial data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

<a id="is-7"></a>

## IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

<a id="is-8"></a>

## IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.31 | [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | 🟢 USEFUL | Why SessionFactory is expensive and shared |
| YT-1.32 | [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) | 🟢 USEFUL | Multiple databases and SessionFactory instances |

<a id="ia-3"></a>

## IA-3 — When would you choose GraphQL over REST for an API?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.33 | [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) | 🟢 USEFUL | Why GraphQL instead of REST |
| YT-1.34 | [19:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1145s) | 🟢 USEFUL | GraphQL query entry point |
| YT-1.35 | [19:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1169s) | 🟢 USEFUL | GraphQL versus REST decision criteria |

<a id="ia-4"></a>

## IA-4 — How does GraphQL field selection compare with REST DTO responses?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.36 | [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | 🟢 USEFUL | GraphQL field-level selection |
| YT-1.37 | [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) | 🟢 USEFUL | REST DTO and field filtering alternatives |
| YT-1.38 | [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) | 🟢 USEFUL | Variable response fields across clients |

<a id="is-9"></a>

## IS-9 — Compare application.properties and application.yml in Spring Boot.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.39 | [22:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1359s) | 🟢 USEFUL | External Spring Boot configuration |
| YT-1.40 | [23:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1380s) | 🟢 USEFUL | Properties versus YAML |
| YT-1.41 | [23:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1418s) | 🟢 USEFUL | Hierarchical YAML configuration |
| YT-1.42 | [24:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1453s) | 🟢 USEFUL | Structured configuration values |

<a id="ia-5"></a>

## IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.43 | [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | 🟢 USEFUL | Distributed transactions in microservices |
| YT-1.44 | [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) | 🟢 USEFUL | Saga versus two-phase commit |
| YT-1.45 | [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) | 🟢 USEFUL | Saga events and compensating actions |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |

<a id="ia-6"></a>

## IA-6 — How would you gather functional and nonfunctional requirements for an e-commerce platform?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.46 | [25:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1555s) | 🟡 INTRO | E-commerce system-design prompt |
| YT-1.47 | [26:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1618s) | 🟢 USEFUL | Functional e-commerce requirements |
| YT-1.48 | [27:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1655s) | 🟢 USEFUL | Nonfunctional requirements |
| YT-1.49 | [28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1717s) | 🟢 USEFUL | Search, cart, order, delivery and notification scope |

<a id="ia-7"></a>

## IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.50 | [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | 🟢 USEFUL | Abusive traffic and peak sale load |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.54 | [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) | 🟢 USEFUL | Rate limiting suspicious requests |

<a id="ia-8"></a>

## IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.51 | [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | 🟢 USEFUL | Client and web/mobile system entry point |
| YT-1.52 | [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) | 🟢 USEFUL | Load balancers for replicated services |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.55 | [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) | 🟢 USEFUL | Search service and microservice boundary |

<a id="ia-9"></a>

## IA-9 — Design product search using a cache, database and search index.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.56 | [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) | 🟢 USEFUL | Redis cache for product search |
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.58 | [36:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2165s) | 🟢 USEFUL | Elasticsearch for product queries |
| YT-1.59 | [37:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2259s) | 🟢 USEFUL | Text search and typo-tolerant indexing |
| YT-1.60 | [38:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2297s) | 🟢 USEFUL | Hot search queries cached in Redis |

<a id="ia-22"></a>

## IA-22 — What tradeoffs affect choosing a database for search versus shopping-cart data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

<a id="id-3"></a>

## ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |

<a id="ia-10"></a>

## IA-10 — How would you model a user's cart, and why might you choose a relational database?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.61 | [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) | 🟢 USEFUL | Cart service data model |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

<a id="ia-11"></a>

## IA-11 — How should cart, product, inventory and user responsibilities be split across services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |
| YT-1.68 | [43:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2638s) | 🟢 USEFUL | Inventory and product service split |
| YT-1.69 | [44:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2683s) | 🟢 USEFUL | Single responsibility for product service |

<a id="ia-21"></a>

## IA-21 — How would backend microservices communicate with each other using HTTP clients?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |

<a id="ia-12"></a>

## IA-12 — How do you avoid overselling the last inventory item when Kafka delivery is delayed?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.64 | [41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) | 🟢 USEFUL | Order and delivery business workflow |
| YT-1.65 | [42:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2521s) | 🟢 USEFUL | Kafka events and inventory reduction |
| YT-1.66 | [42:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2561s) | 🟢 USEFUL | Overselling due to delayed consumers |
| YT-1.67 | [43:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2599s) | 🟢 USEFUL | Inventory consistency reconsidered |

<a id="ia-13"></a>

## IA-13 — How would you implement delivery-partner assignment with asynchronous events?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.70 | [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) | 🟢 USEFUL | Assigning delivery partners |
| YT-1.71 | [46:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2765s) | 🟢 USEFUL | Structured delivery partner storage |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |
| YT-1.73 | [48:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2896s) | 🟢 USEFUL | Delivery assignment need not be immediate |
| YT-1.74 | [48:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2930s) | 🟢 USEFUL | Kafka event-driven delivery processing |

<a id="ia-14"></a>

## IA-14 — How would you deliver order-status notifications by email and SMS?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.75 | [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) | 🟢 USEFUL | Email and SMS notifications |

<a id="ia-15"></a>

## IA-15 — Design an event-driven order-tracking system with a suitable database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.76 | [50:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3000s) | 🟢 USEFUL | Order tracking requirement |
| YT-1.78 | [51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) | 🟢 USEFUL | Tracking events through Kafka |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |
| YT-1.80 | [53:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3195s) | 🟢 USEFUL | Delivery confirmation asynchronously |

<a id="ia-16"></a>

## IA-16 — What data would you collect for logs and commerce analytics?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.77 | [50:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3038s) | 🟢 USEFUL | Logs and sales analytics |

<a id="id-1"></a>

## ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.81 | [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | 🟢 USEFUL | Slow SQL query diagnosis |
| YT-1.82 | [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) | 🟢 USEFUL | Indexing and query profiling |

<a id="id-2"></a>

## ID-2 — Explain table partitioning versus database sharding.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.83 | [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | 🟢 USEFUL | Database partitioning |
| YT-1.84 | [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) | 🟢 USEFUL | Sharding versus partitioning |

<a id="ia-20"></a>

## IA-20 — How would you diagnose Kafka consumer lag in a distributed system?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.85 | [55:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3359s) | 🟢 USEFUL | Kafka consumer lag interview question — no clear tested remedy demonstrated |

<a id="ia-17"></a>

## IA-17 — Why use a CDN for an e-commerce product catalog?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.86 | [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) | 🟢 USEFUL | CDN for images and static content |

<a id="ia-18"></a>

## IA-18 — How would you autoscale services when traffic surges during holiday sales?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.87 | [58:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3529s) | 🟢 USEFUL | Autoscaling during sales spikes |

<a id="ia-19"></a>

## IA-19 — How would you implement infinite scroll with pagination, prefetching and loading feedback?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.88 | [59:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3592s) | 🟢 USEFUL | Backend and frontend pagination prompt |
| YT-1.89 | [1:00:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3628s) | 🟢 USEFUL | Lazy loading and infinite scrolling |
| YT-1.91 | [1:01:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3719s) | 🟢 USEFUL | Latency between scrolling and API response |
| YT-1.92 | [1:02:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3761s) | 🟢 USEFUL | Prefetching before viewport end |
| YT-1.93 | [1:03:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3786s) | 🟢 USEFUL | Skeleton states, debounce and throttle |

<a id="is-11"></a>

## IS-11 — How would you implement backend pagination using Spring Data JPA?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.90 | [1:01:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3678s) | 🟢 USEFUL | JPA pagination and batch fetching |

<a id="ic-1"></a>

## IC-1 — What Git branching and release promotion workflow have you used?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |

<a id="ic-2"></a>

## IC-2 — How do feature branches progress through QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |

<a id="is-10"></a>

## IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.97 | [1:05:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3946s) | 🟢 USEFUL | Spring profiles with per-environment properties |

<a id="ic-3"></a>

## IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |

<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |
| YT-1.100 | [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) | 🟢 USEFUL | Continuous integration checks |
| YT-1.101 | [1:08:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4122s) | 🟢 USEFUL | Continuous delivery and deployment |

<a id="ic-5"></a>

## IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.102 | [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | 🟢 USEFUL | Dockerfile, image and container |

<a id="ic-6"></a>

## IC-6 — How would you run and scale ten microservices with Kubernetes?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.103 | [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | 🟢 USEFUL | Managing multiple microservice containers |
| YT-1.104 | [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) | 🟢 USEFUL | Kubernetes orchestration and replicas |

<a id="ic-7"></a>

## IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.105 | [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | 🟢 USEFUL | Repeated Kubernetes pod crashes and CrashLoopBackOff scenario |
| YT-1.106 | [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) | 🟢 USEFUL | Crash triage, logs and PagerDuty |

<a id="ic-8"></a>

## IC-8 — How would you roll back a broken deployment to a previous container image?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.107 | [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | 🟢 USEFUL | Rollback to previous application version |
| YT-1.108 | [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) | 🟢 USEFUL | Release versioning and rollback workflow |

<a id="ic-9"></a>

## IC-9 — What is infrastructure as code, and how would you use Pulumi for cloud alerts?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.109 | [1:14:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4453s) | 🟢 USEFUL | Infrastructure as code with Pulumi |
| YT-1.110 | [1:14:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4481s) | 🟢 USEFUL | Azure alerting and infrastructure automation |

<a id="it-1"></a>

## IT-1 — How should a team interpret a claim of 90 to 95 percent unit-test coverage?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.111 | [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | 🟢 USEFUL | High test coverage question |

<a id="it-2"></a>

## IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.112 | [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | 🟢 USEFUL | JUnit tests and mocked dependencies |

<a id="it-3"></a>

## IT-3 — How is SonarQube used for static analysis and code quality checks?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.113 | [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) | 🟢 USEFUL | SonarQube and static analysis |

<a id="it-4"></a>

## IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.114 | [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | 🟢 USEFUL | Do not test trivial getters just for coverage |
| YT-1.115 | [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) | 🟢 USEFUL | Exclude DTO boilerplate from coverage |

<a id="it-5"></a>

## IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.116 | [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | 🟢 USEFUL | Integration tests for entities and services |
| YT-1.117 | [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) | 🟢 USEFUL | Microservice end-to-end testing |
| YT-1.118 | [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) | 🟢 USEFUL | Avoid real cross-service calls in unit tests |
| YT-1.119 | [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) | 🟢 USEFUL | Use separate integration/system-test suites |

<a id="is-12"></a>

## IS-12 — What is reactive programming in Spring WebFlux, and how do Mono and Flux differ?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.120 | [1:22:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4951s) | 🟡 INTRO | Introduction to reactive Spring applications |
| YT-1.121 | [1:22:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4966s) | 🟢 USEFUL | Blocking versus nonblocking I/O |
| YT-1.122 | [1:23:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5013s) | 🟢 USEFUL | Mono and Flux overview |
| YT-1.123 | [1:23:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5032s) | 🟢 USEFUL | Project Reactor in Spring |

<a id="ic-10"></a>

## IC-10 — Compare Maven and Gradle as Java build tools.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.124 | [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) | 🟢 USEFUL | Maven versus Gradle question |

<a id="ic-11"></a>

## IC-11 — What is the purpose of pom.xml and how does Maven resolve dependencies?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.125 | [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) | 🟢 USEFUL | Interview question switches to why pom.xml is used |
| YT-1.126 | [1:25:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5136s) | 🟢 USEFUL | Purpose of pom.xml |

<a id="ic-12"></a>

## IC-12 — Compare Kanban and Scrum and explain how they affect a team's delivery workflow.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.127 | [1:26:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5212s) | 🟢 USEFUL | Kanban versus Scrum in team workflow |

<a id="ij-1"></a>

## IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.128 | [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | 🟢 USEFUL | ConcurrentHashMap internal design question |
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |
| YT-1.131 | [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) | 🟢 USEFUL | Legacy segment-lock explanation caveat |

<a id="ij-3"></a>

## IJ-3 — How does HashMap fail-fast iteration compare with ConcurrentHashMap iteration?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |

<a id="ij-2"></a>

## IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.132 | [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | 🟢 USEFUL | Using employee objects as HashMap keys |
| YT-1.133 | [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) | 🟢 USEFUL | equals and hashCode contract |

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
