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

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [2:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=175s) so generally we enforce the security mainly on the back end itself<br>[3:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=186s) because uh the client browsers uh it is secured like we can have like multiple browsers running but main thing which we have to ensure is our servers are running fine so we generally go with<br>[3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) some of the security features like JWT uh because generally we go with the HTTP rest apis these are like stateless applications which means like when every time when you make a request you don't | I secure a Spring Boot API by making the backend check every request, not by trusting the browser. When a user signs in, the identity provider gives them an access token. The frontend sends it with API requests, and Spring Security checks that it's genuine, hasn't expired, and permits the action. For example, a normal customer should never access an admin endpoint. The simple rule is: the frontend offers the experience, but the backend makes the security decision. |


<a id="is-5"></a>

## IS-5 — How do access-token expiry and refresh tokens work?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.6 | [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | 🟢 USEFUL | Token expiration and refresh tokens |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| **No substantive response; only this brief acknowledgement is captured.**<br>[4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) yes yeah exactly | An access token is a short-lived pass to call an API. When it expires, the user shouldn't necessarily have to sign in again. The app can use a properly protected refresh token to request a new access token from the authorization server. For example, while someone browses an online store, their session can continue without interrupting every few minutes. Refresh tokens need strong protection and sometimes rotation or revocation. Short-lived access plus carefully managed refresh is the balance. |


<a id="is-2"></a>

## IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.7 | [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | 🟢 USEFUL | Okta OAuth authorization server |
| YT-1.8 | [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) | 🟢 USEFUL | Authentication redirect and authorization flow |
| YT-1.9 | [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) | 🟢 USEFUL | Callback URLs and identity-provider configuration |
| YT-1.10 | [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) | 🟢 USEFUL | Frontend-to-Okta-to-backend flow |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) uh I generally used uh OCTA o 2.0 U that's that's that's I think that's one of the popularly getting used uh<br>[4:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=272s) authentication and authorization tool so and it's uh spring also comes with a spring security uh which I prefer like also return on top of this so this is the main thing which I have used correct<br>[4:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=286s) I agree that OCTA you have used as authorization servers and Spring Security is something which properly integrates with the OCTA parts so yes completely agree on that front now my | I use Okta to handle sign-in, while Spring Security protects the API. For example, a user clicks Login, signs in through Okta, and the application receives tokens through the configured OAuth/OpenID Connect flow. When the user calls our order API, the backend validates the access token and checks permissions. For a browser app, I would normally use authorization code with PKCE. Okta confirms who signed in; our API still decides what that person can do. |


<a id="is-3"></a>

## IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.11 | [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | 🟢 USEFUL | How a backend validates JWTs |
| YT-1.12 | [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) | 🟢 USEFUL | JWT signature and payload discussion — JWT payload is encoded, not automatically encrypted |
| YT-1.13 | [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) | 🟢 USEFUL | Questionable JWT validation explanation — WARNING: candidate's token-validation claim is incorrect; validate signature and claims |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [7:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=434s) the token what uh it's getting generated it's B is based on<br>[7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) some hashing algorithms it means it it's a one way like u based on that hash code if I just use JWT uh which can if you hash back it like we can get like three part out of it so we I think one of the<br>[7:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=461s) part is signature which is just to authenticate whether this hash is corrupted or some someone like uh changed it or not hacked it or not uh but in our case if let's assume like if | A JWT is like a signed entry pass. Before trusting it, my Spring Boot API checks the signature, the issuer, who the token is meant for, and whether it has expired. Then I check the user's permission for the request. For example, changing the word 'admin' inside the token should break its signature. I use Spring Security's JWT support instead of writing my own verification. The key point: reading a token is easy; proving it's genuine is what matters. |


<a id="is-4"></a>

## IS-4 — What information must not be stored in JWT claims, and why?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.14 | [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | 🟢 USEFUL | Sensitive data inside JWT claims |
| YT-1.15 | [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) | 🟢 USEFUL | Password and JWT payload safety |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [9:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=553s) uh no I think it's Works based on like a hashing is only like a one way of uh it's called like one way like<br>[9:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=567s) mapping it means like from the the keywords we can get to know like what's the hash code but other way can't be possible so you can't get to know the actual password sorry I said password<br>[9:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=577s) but you can't get to know the password so generally anyone can't get to know only the user know his own passwords so when we save it in the database so it's always be the hashing so we never save | I treat a JWT payload like a postcard: someone holding the token can usually read what's written on it. That's why I never put passwords, secrets, or unnecessary personal information inside. For example, including a customer's password in a token would expose it to anyone who gets a copy. A signature prevents undetected changes; it doesn't hide the text. My rule is simple: keep claims minimal, protect tokens, and never mistake encoding for encryption. |


<a id="is-6"></a>

## IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.17 | [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | 🟢 USEFUL | Duplicate scheduled jobs across replicas |
| YT-1.18 | [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) | 🟢 USEFUL | ShedLock for single scheduler execution |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [10:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=653s) uh yeah I mean generally we go with the spring scheduler but the drawback as you mentioned uh if there are multiple<br>[11:04](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=664s) instances the spring Schuler can't able to handle this instance it end up with running on all the three instance so we want something like a single turn Behavior here like for that we can go<br>[11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) with something called shedlock so how it orchestrate is like rather than uh it will let it to run only once and like and ra for the all the instances so that's how internal architectures are | If I run the same Spring scheduler on three servers, all three may execute the job. That's a problem if the job must send only one email or create only one record. I would use a shared lock, such as ShedLock backed by the database, so only one instance runs at a time. I would also make the job safe to retry after a crash. A scheduler knows when to run; a shared lock helps decide who runs. |


<a id="ia-1"></a>

## IA-1 — Explain cache-aside caching using Redis and a database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.19 | [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | 🟡 INTRO | Caching discussion begins |
| YT-1.20 | [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) | 🟢 USEFUL | Redis cache-aside lookup |
| YT-1.21 | [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) | 🟢 USEFUL | In-memory caching and latency |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) uh the caching generally uh I<br>[11:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=701s) mean uh either we can use the third party which is already available so which is like uh redis is one of the popular caching uh it's nowadays which we use uh to enhance the performance<br>[11:51](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=711s) there are few datas which we find like frequently are getting used so rather than hitting the database which takes some additional time as a latency so we can use this caching which is like | Redis helps me avoid asking the database the same question again and again. Suppose a popular product page gets 10,000 requests. I first look for its details in Redis. If they're there, I return them quickly. If not, I read the database, put a copy in Redis, and return it. That's called cache-aside. The trick is remembering that Redis is a fast copy, while the database remains the source of truth. |


<a id="ia-2"></a>

## IA-2 — How would you control stale cached data using TTL and consistency requirements?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.22 | [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | 🟢 USEFUL | Cache TTL and freshness |
| YT-1.23 | [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) | 🟢 USEFUL | Stale cached data and TTL tradeoffs |
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) uh so generally for the server it can't get to know whether the data is dirty or not because only the database has a clear idea whether this data was corrupted so there could<br>[13:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=838s) be be a chances of reading this diry data but this kind of data we keep this kind of data especially for the applications like where some datas need not to be accurate like for example if<br>[14:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=849s) you use Twitter so we don't want like what I see on my table sorry page is need not to be like as accurate as yours so when we can compromise on the consistency we can go with like this | A cache is useful only if we know how fresh its data needs to be. For example, an old product description may be acceptable for a minute, but an incorrect bank balance is not. I use a time-to-live to expire cached entries and invalidate or update them when important data changes. I also plan for timing races between a database write and a cache read. The question isn't 'How long can we cache?'; it's 'How wrong can this data safely be?' |


<a id="id-4"></a>

## ID-4 — How do consistency needs differ between cached social content and financial data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) if it's highly Financial then I would say dirty read can't be something which we can compromise because we can't we don't want to see<br>[14:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=872s) like the account balance something inaccurate on the two different accounts | Not every piece of data needs to be fresh to the exact same millisecond. A social feed can often show a post a few seconds late without hurting anyone. A bank balance before a withdrawal is a different story: we need the authoritative value and transaction checks. I may cache read-heavy feed data, but I take a much stricter approach to financial decisions. Consistency is a business promise, not just a database setting. |


<a id="is-7"></a>

## IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) uh yes so session level uh is called L1 caching and session Factory is the L2 so by default we enable the session level caching which is like limited to particular session so<br>[16:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=970s) but if you want some data which should be like could be cached across the all the sessions then we put it in the L2 level caching which is under the session Factory | Hibernate has two useful cache levels. The first-level cache belongs to one Session and is always there. If I read the same entity twice in that session, Hibernate can avoid a second database fetch. The optional second-level cache can share eligible entity data across sessions using a configured provider. For example, product categories that rarely change might benefit from it. The memory trick is: L1 belongs to one conversation with the database; L2 can serve many conversations. |


<a id="is-8"></a>

## IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.31 | [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | 🟢 USEFUL | Why SessionFactory is expensive and shared |
| YT-1.32 | [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) | 🟢 USEFUL | Multiple databases and SessionFactory instances |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) U first thing is like it's a costly<br>[17:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1020s) operation I would say but I mean in the normal words U this as same as like creating the instance of the database so we generally want it to be like U highly uh synchronized uh applications so that<br>[17:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1032s) no two uh interactions can corrupt the datas so when we make it as single turn so that uh every time every new sessions we use the same uh sorry every uh New Creations will create the only one | I reuse SessionFactory because building it takes work: it holds Hibernate's mapping and database configuration. It isn't a single database connection. Think of it as a factory that creates many short-lived Sessions, usually using pooled connections underneath. If my application connects to three separately configured databases, I generally set up an appropriate factory or persistence unit for each. Reuse the factory; open and close sessions for the actual work. |


<a id="ia-3"></a>

## IA-3 — When would you choose GraphQL over REST for an API?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.33 | [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) | 🟢 USEFUL | Why GraphQL instead of REST |
| YT-1.34 | [19:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1145s) | 🟢 USEFUL | GraphQL query entry point |
| YT-1.35 | [19:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1169s) | 🟢 USEFUL | GraphQL versus REST decision criteria |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) uh generally U it's not a limitation of the rest API it's just<br>[18:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1123s) like when we go with the rest API there are so many end points come to picture like it's very hard for the any client applications or any like third party to remember this so like for example if I<br>[18:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1133s) have like a a student as the uh main entity and if you have like all the crude operation then like it end up with like so many end points for suent TBL and similarly for like account again | I choose GraphQL when different clients need different pieces of the same data. For example, a mobile screen might need only a product's name and price, while the website needs reviews and images too. GraphQL lets each client ask for the fields it needs. REST still works very well for straightforward resource APIs. So I don't choose GraphQL because it's trendy. I choose it when flexible queries genuinely make the client simpler, while controlling query cost and permissions. |


<a id="ia-4"></a>

## IA-4 — How does GraphQL field selection compare with REST DTO responses?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.36 | [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | 🟢 USEFUL | GraphQL field-level selection |
| YT-1.37 | [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) | 🟢 USEFUL | REST DTO and field filtering alternatives |
| YT-1.38 | [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) | 🟢 USEFUL | Variable response fields across clients |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) returned with the graph we can also limit in the rest API as well based on like what kind of dto we are returning because like uh yeah I I didn't go in depth about this but uh in rest AP also<br>[21:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1269s) we can limit what response we are responding back we also come up with something called Json ignore and yeah some crucial Fields if you don't want to ex we don't want to export we can at the<br>[21:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1279s) rate and out with Json ignore ignore so yeah but I feel like it's still like too much of laborious task to do this using rest API which can be easily automated with the graph | GraphQL lets the caller choose fields in a query. For example, a customer screen can request just an employee's ID and name instead of the whole employee record. REST can return smaller responses too, using DTOs or field-selection options. The difference is that GraphQL makes client-driven selection a central feature. I would use whichever approach keeps the API predictable, secure, and easy to maintain. Less unnecessary data is good; extra complexity isn't always worth it. |


<a id="is-9"></a>

## IS-9 — Compare application.properties and application.yml in Spring Boot.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.39 | [22:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1359s) | 🟢 USEFUL | External Spring Boot configuration |
| YT-1.40 | [23:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1380s) | 🟢 USEFUL | Properties versus YAML |
| YT-1.41 | [23:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1418s) | 🟢 USEFUL | Hierarchical YAML configuration |
| YT-1.42 | [24:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1453s) | 🟢 USEFUL | Structured configuration values |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [23:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1380s) uh actually uh uh much there is no<br>[23:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1395s) difference it's just like the way we write the files uh the structure is different the yl is like yet another markup language as a name indicate so the main problem with like normal the<br>[23:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1407s) property file the application do property we use the Dot Structure so so the thing is like we have to keep on repeating the same prefix for uh every uh changes for example it has to be like | Both application.properties and application.yml tell Spring Boot how to run. The biggest difference is how they look. In properties, I'd write server.port=8080. In YAML, I'd place port beneath server, which is easier to read when settings have several levels. Both can produce the same result. I choose the format my team can understand and maintain consistently; the format itself doesn't make the application faster or safer. |


<a id="ia-5"></a>

## IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.43 | [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | 🟢 USEFUL | Distributed transactions in microservices |
| YT-1.44 | [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) | 🟢 USEFUL | Saga versus two-phase commit |
| YT-1.45 | [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) | 🟢 USEFUL | Saga events and compensating actions |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) uh so when it comes to distributed transactions uh it's easy to handle that in the monolith architecture<br>[24:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1484s) because we can have one transaction and write all the operations we want to perform but in case of distributed we uh bate the functionalities to different micros service the main problem is if<br>[24:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1496s) something goes wrong then we have to roll back but since it is under in different transactions we have a I think two-way of approach so whether we can go with synchronized or asynchronized I | A Saga helps several microservices complete one business process without pretending they share a single database transaction. Picture placing an order: reserve stock, take payment, and create the order. If payment fails, we release the stock through a compensating action. Two-phase commit tries to coordinate an atomic commit across participants, but can be harder to operate and less available. A Saga doesn't magically roll back the whole world; it plans how to recover from each step. |


<a id="ia-6"></a>

## IA-6 — How would you gather functional and nonfunctional requirements for an e-commerce platform?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.46 | [25:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1555s) | 🟡 INTRO | E-commerce system-design prompt |
| YT-1.47 | [26:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1618s) | 🟢 USEFUL | Functional e-commerce requirements |
| YT-1.48 | [27:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1655s) | 🟢 USEFUL | Nonfunctional requirements |
| YT-1.49 | [28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1717s) | 🟢 USEFUL | Search, cart, order, delivery and notification scope |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1595s) uh sure so uh generally we say the<br>[26:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1608s) e-commerce I would take U either flip cart or Amazon as an example here so if if I get this kind of questions first I would think what could be the functional requ requirement and what are<br>[26:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1618s) non-functional requirement because functional requirement is something like uh business steam or some customer would specify what kind of requirements we want so in the e-commerce first thing is | Before drawing an e-commerce system, I ask what customers need to do and how much traffic we expect. The basic flow is search, cart, checkout, payment, and order tracking. Then I ask about scale, response time, security, and what happens when a service fails. For example, selling ten products a day is different from handling a flash sale with a million visitors. Good system design starts with good questions, not with drawing twenty microservices. |


<a id="ia-7"></a>

## IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.50 | [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | 🟢 USEFUL | Abusive traffic and peak sale load |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.54 | [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) | 🟢 USEFUL | Rate limiting suspicious requests |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) handlers like it will keep track of like how many requests are coming from like same uh IP address so if if it find it like uh if the the number of request is miscellaneous like it's not something uh<br>[33:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1981s) it's like active uh user request in that case we can uh it will like stop the user to hit that part so which we call that as rate limits yeah rate limits that's what sorry that's what I was<br>[33:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1994s) trying to say no problem okay yeah I yeah I don't have any filter kind of icons so I would have used that here so okay no problem uh um okay so then we have like different | I protect an e-commerce API by limiting how many requests a client can send in a short time. For example, one account shouldn't be allowed to call product search thousands of times per second. I put rate limits at the API gateway, and I can add WAF rules or bot protection for suspicious traffic. I wouldn't rely only on IP addresses because many real users can share one IP. Protecting the system means slowing abuse without blocking genuine shoppers. |


<a id="ia-8"></a>

## IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.51 | [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | 🟢 USEFUL | Client and web/mobile system entry point |
| YT-1.52 | [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) | 🟢 USEFUL | Load balancers for replicated services |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.55 | [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) | 🟢 USEFUL | Search service and microservice boundary |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) simple design first then I'll keep on add the enhancement based on the non-functionality as well so yeah generally we have a client here client could be either uh like a mobile or it<br>[31:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1897s) could be uh web or any uh lab yeah this has to be like a responsive web screen so that every different resolution can see that uh HTML page in a clear way and um there<br>[31:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1912s) could be many uh users because since we are talking about the e-commerce website we can come up with like um millions of user in know we call that as like a daily active users So based on that we | I would start with the customer, then follow one request through the system. The browser hits a CDN or gateway, a load balancer selects a healthy application instance, and the right service handles the request. Search might use a cache and search index; orders and payments need reliable storage and clear ownership. For example, if one search instance crashes, another should keep serving customers. I design for the customer journey first, then scale and failures. |


<a id="ia-9"></a>

## IA-9 — Design product search using a cache, database and search index.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.56 | [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) | 🟢 USEFUL | Redis cache for product search |
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.58 | [36:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2165s) | 🟢 USEFUL | Elasticsearch for product queries |
| YT-1.59 | [37:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2259s) | 🟢 USEFUL | Text search and typo-tolerant indexing |
| YT-1.60 | [38:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2297s) | 🟢 USEFUL | Hot search queries cached in Redis |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) okay so this generally cash the uh the data like all the items which are coming<br>[34:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2095s) from the inventories so this data need not to be accurate like sometimes we can search the product but even though if you don't available in the car in the inventory so this need not be like 100%<br>[35:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2105s) consistence it can be like uh eventual consistence as well so that's totally fine uh so and generally we can go with the database here uh of no SQL or SQL but I was thinking | For product search, I separate where product data is owned from how people search it. A product database stores the real catalog. A search index such as Elasticsearch makes text and typo-tolerant searches fast. Redis can hold common search results so we don't repeat expensive queries. For example, thousands of people searching 'running shoes' may share a cached result. But stock and price must be checked again when the customer actually buys. |


<a id="ia-22"></a>

## IA-22 — What tradeoffs affect choosing a database for search versus shopping-cart data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) we can go with the Cassandra or mongodb it's up to I mean there's no problem but it's just like if you use Cassandra it's provide eventual consistency so I I will go with the Cassandra here okay so so<br>[35:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2143s) basically you're going with no SQL for s Service yeah no SQL so it can be uh yeah it's need not be like no SQL but I find it here more relevant as a Cassandra I uh | I choose databases based on the question each service needs to answer. Product search benefits from a search index; a cart may benefit from SQL transactions; order history may fit a simple relational table. For example, storing products in MongoDB doesn't automatically give customers good full-text search. We still might need Elasticsearch. I compare access patterns, consistency, scale, and operational cost before deciding. Pick the database for the job, not because every service needs a different one. |


<a id="id-3"></a>

## ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) I will go with the Cassandra here okay so so<br>[35:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2143s) basically you're going with no SQL for s Service yeah no SQL so it can be uh yeah it's need not be like no SQL but I find it here more relevant as a Cassandra I uh | I wouldn't choose SQL or NoSQL just because a service is called 'search' or 'cart.' I'd ask what it reads and what must never go wrong. For example, product descriptions might live in SQL or a document store, while search uses a separate index. Cart and inventory updates often need reliable transactions. Order tracking may be a simple relational history table. Use the simplest database that meets the actual data and consistency needs. |


<a id="ia-10"></a>

## IA-10 — How would you model a user's cart, and why might you choose a relational database?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.61 | [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) | 🟢 USEFUL | Cart service data model |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [39:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2342s) the cart service like uh when user add to the cut it means like U it has to be like a map so I generally like map between like uh this user and his all the items so it could be like uh one to<br>[39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) many mappings so generally if it's a mapping uh it could be debatable but I can go with the SQL database so here it could be uh my SQ mycle is better suit uh because there is<br>[39:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2370s) something called a cap algorithm which is called consistency availability and the I forgot about the last one it is uh yeah so yeah so in my case I need complete consistency because uh and the | A shopping cart is naturally a relationship between a user and the products they selected. I might store it in SQL using a cart table and cart-item rows, each with product ID and quantity. When the same item is added twice, I update its quantity safely rather than creating a confusing duplicate. A relational database is a solid option because updates and relationships are clear. The important part isn't the brand of database—it's keeping the cart correct. |


<a id="ia-11"></a>

## IA-11 — How should cart, product, inventory and user responsibilities be split across services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |
| YT-1.68 | [43:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2638s) | 🟢 USEFUL | Inventory and product service split |
| YT-1.69 | [44:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2683s) | 🟢 USEFUL | Single responsibility for product service |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) since it is a micros service it doesn't have all the<br>[40:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2442s) compete information it just perform one single uh responsibility so I can uh I mean in the behind the picture I can go with either uh rest template or a f client algorithms to communicate with<br>[40:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2455s) the services but but uh but when it comes to system design uh I don't want to go in depth about the uh coding but when it comes to uh place order so when user place the order | I split microservices around business responsibilities, not just names on a diagram. The catalog describes products, inventory knows what stock is available, the cart remembers selections, and the order service manages purchases. For example, the product page can say 'in stock,' but only inventory should decide whether the last unit can be reserved. Each service owns its data and communicates through clear APIs or events. Good boundaries prevent one problem from spreading everywhere. |


<a id="ia-21"></a>

## IA-21 — How would backend microservices communicate with each other using HTTP clients?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.63 | [40:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2425s) | 🟢 USEFUL | Service-to-service communication |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [40:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2442s) I can go with either uh rest template or a f client algorithms to communicate with<br>[40:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2455s) the services but but uh but when it comes to system design uh I don't want to go in depth about the uh coding but when it comes to uh place order so when user place the order<br>[41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) assign it to delivery patterns so here we are to use also use something called Saga design patterns because uh these three things I mean uh placing the order assign the delivery and also | For a quick request-and-response between Spring services, I use a clear HTTP client such as RestClient or OpenFeign. For example, an order service may need to check customer details before accepting a request. I set timeouts, secure the call, and handle the case where the customer service is down. If the work doesn't need an immediate answer, an event may be better. The best communication style depends on whether the business process must wait. |


<a id="ia-12"></a>

## IA-12 — How do you avoid overselling the last inventory item when Kafka delivery is delayed?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.64 | [41:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2472s) | 🟢 USEFUL | Order and delivery business workflow |
| YT-1.65 | [42:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2521s) | 🟢 USEFUL | Kafka events and inventory reduction |
| YT-1.66 | [42:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2561s) | 🟢 USEFUL | Overselling due to delayed consumers |
| YT-1.67 | [43:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2599s) | 🟢 USEFUL | Inventory consistency reconsidered |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [42:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2521s) maybe in the place order U I use some I use called Kafka here because whenever we place the order item has to get<br>[42:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2534s) reduced from the inventory and there is some periodic update has to be done so that next user won't get any problem of like uh ordering the same item but eventually it will come up with like no<br>[42:26](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2546s) items are available so I need a Kafka here uh so that once I place the order u i can update that in my inventory so that my no SQL will get updated correct so this CF will be over this so uh when | Kafka is great for telling other services that something happened, but I wouldn't use a delayed event to decide whether the last item can be sold. Imagine two customers buying the only remaining laptop at the same moment. Inventory must reserve that laptop atomically before we confirm either order. After that, Kafka can safely notify shipping or analytics using reliable publishing. The takeaway is simple: confirm stock first; announce the result second. |


<a id="ia-13"></a>

## IA-13 — How would you implement delivery-partner assignment with asynchronous events?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.70 | [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) | 🟢 USEFUL | Assigning delivery partners |
| YT-1.71 | [46:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2765s) | 🟢 USEFUL | Structured delivery partner storage |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |
| YT-1.73 | [48:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2896s) | 🟢 USEFUL | Delivery assignment need not be immediate |
| YT-1.74 | [48:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2930s) | 🟢 USEFUL | Kafka event-driven delivery processing |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [45:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2748s) for uh uh assigning the delivery Partners uh yeah so uh we also need<br>[46:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2765s) a sign delivery uh Partners so we should have one more service to keep uh the keep like uh we need a table to keep like uh all the delivery Partners which are available so<br>[46:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2788s) so I go with the SQL here because uh I mean I find it like all the deliveries partner have like more structured data so that's the main intention so uh and like what kind of delivery they're | I wouldn't make a customer wait for a delivery partner to be assigned before showing 'Order placed.' Once payment and inventory are handled, the order service can publish an event. A delivery service picks it up, finds an available partner, and records the assignment. If nobody is available yet, the order stays pending and the system retries. For example, a food-delivery app can confirm an order before a rider accepts it. Keep checkout quick and delivery reliable. |


<a id="ia-14"></a>

## IA-14 — How would you deliver order-status notifications by email and SMS?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.75 | [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) | 🟢 USEFUL | Email and SMS notifications |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [49:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2958s) uh I can use the same Kafka to trigger another notifications for the notification part so we have a notification service and uh this based on the user uh preference<br>[49:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2972s) like if user just want the SMS or if user want it to be email kind of notifications and everything uh based on that we can uh have a s i mean notification handlers it could be SMS or<br>[49:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2985s) it could be uh email or it could be any other different way of uh intimating the users yes and there is one thing I yet to write is something called uh uh tracking the orders once the delivery | I would have one notification service listen for events such as OrderPlaced or OrderShipped. It checks whether the customer prefers email, SMS, or both, and sends the right message. For example, one purchase should produce one order-confirmation email even if Kafka redelivers the event. That means using an idempotency key and retrying temporary delivery failures. Notifications are important, but an email-provider outage should never cancel a valid order. |


<a id="ia-15"></a>

## IA-15 — Design an event-driven order-tracking system with a suitable database.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.76 | [50:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3000s) | 🟢 USEFUL | Order tracking requirement |
| YT-1.78 | [51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) | 🟢 USEFUL | Tracking events through Kafka |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |
| YT-1.80 | [53:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3195s) | 🟢 USEFUL | Delivery confirmation asynchronously |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) we can have like a same Kafka uh notifications which uh help us to like uh put an entry in our uh table which help us to track the uh items okay it could be<br>[51:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3092s) uh since I said items are like could be in any different structure I can keep it as no SQL here also so this generally like contain the historical data in a chronological order<br>[51:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3105s) like uh and also like there will be a flag which says like whether it is delivered or not so that help us to like keep track of like whether the item is delivered and | I track an order as a history of events, not just one changing word. For example: placed at 10:00, packed at 11:00, shipped at 14:00, and delivered tomorrow. Each event stores the order ID, status, and time. A relational table often handles this well, and Kafka can deliver updates from other services. I also guard against duplicate or out-of-order events. Customers want a clear story of where their order is, and the data should tell that story. |


<a id="ia-16"></a>

## IA-16 — What data would you collect for logs and commerce analytics?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.77 | [50:38](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3038s) | 🟢 USEFUL | Logs and sales analytics |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [50:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3048s) we can have some analytic tool on top of this it could be like Apache spark or something and then we can decide like okay we can have these kind of items in<br>[50:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3059s) our inventory in our future uh something like that or something we can add a discount or something uh which we see it on like on every holidays uh and for the tracking the product so once the<br>[51:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3072s) delivery part is also assigned so uh we can have like a same Kafka uh notifications which uh help us to like uh put an entry in our uh table which help us to track the uh items okay it could be | I separate two questions: 'Is the system healthy?' and 'How is the business doing?' Logs and metrics help engineers find failed orders or slow APIs; business events help us understand popular products, sales, and returns. For example, a spike in checkout errors needs an alert, while rising demand for shoes belongs in a sales dashboard. I avoid logging passwords or unnecessary personal data. Good data should lead to a decision, not just fill storage. |


<a id="id-1"></a>

## ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.81 | [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | 🟢 USEFUL | Slow SQL query diagnosis |
| YT-1.82 | [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) | 🟢 USEFUL | Indexing and query profiling |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3250s) uh the first thing is like I need to figure it out what is why it is<br>[54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) taking time so couple of Reason could be possible one is uh if the query is taking time because uh it lack with the indexing then it's better we can add a index because indexing is nothing but a<br>[54:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3274s) compound of data structure we use to get the items in a fast way so so that's the first thing I will check I mean it's called analyzing the query uh or profiling the query so get to know | When a SQL query is slow, I measure before changing anything. I find the exact query, inspect its execution plan, and check whether it scans too many rows or misses a useful index. For example, searching a million orders by customer ID may be slow without the right index. I then test the change and watch its effect on reads and writes. Partitioning can help some workloads, but I'd never start by splitting the database just because one query is slow. |


<a id="id-2"></a>

## ID-2 — Explain table partitioning versus database sharding.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.83 | [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | 🟢 USEFUL | Database partitioning |
| YT-1.84 | [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) | 🟢 USEFUL | Sharding versus partitioning |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3296s) there is no difference between much in the sharding and uh partitioning<br>[55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) but the main difference is sharding means like we keep the database in a different uh servers like it's like a same uh same table but we keep it in a different places whereas like in<br>[55:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3319s) partitioning it comes under the same servers but replica not replica like the partitioning happens in the same servers so since the e-commerce can be one in us one in India and everything so | Partitioning and sharding both split data, but for different reasons. Partitioning divides a table into manageable pieces within a database setup, such as orders by month. Sharding spreads responsibility across separate database instances, perhaps by customer region or ID. For example, one large orders table could be partitioned by date before the business ever needs multiple shards. Partitioning helps organize and query data; sharding helps distribute ownership and scale, but adds complexity. |


<a id="ia-20"></a>

## IA-20 — How would you diagnose Kafka consumer lag in a distributed system?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.85 | [55:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3359s) | 🟢 USEFUL | Kafka consumer lag interview question — no clear tested remedy demonstrated |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [56:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3377s) Kafka comes with the resilient uh it's one of the resilient feature of the Kafka is like if anything goes wrong or like if something is going uh failures uh Kafka Works in a concept of like uh<br>[56:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3389s) multiple uh Brokers so there will be like leaders and other one is like a followers or a worker nodes worker Brokers so | Kafka consumer lag means messages are arriving faster than a consumer group is finishing them—or the consumers have stopped making progress. I first check lag by partition, consumer errors, processing time, and slow downstream services. For example, if each message needs a slow database call, adding brokers won't fix that bottleneck. I may optimize processing or increase consumers, up to the useful partition limit. Fix the slow consumer, not just the number on the dashboard. |


<a id="ia-17"></a>

## IA-17 — Why use a CDN for an e-commerce product catalog?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.86 | [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) | 🟢 USEFUL | CDN for images and static content |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [57:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3464s) we could also add it is something called CDN uh generally to keep the static datas the the thing what I'm thinking about is like there are images uh and also few datas which are like<br>[57:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3476s) same like for example if you're booking for pen I mean it's like a common image which we can show so we can use something called CDN It generally comes like a web symbol I think there are popular CDN<br>[58:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3488s) available like Aline and uh and uh Cloud flare there are like popular ones where uh which keep the datas geographically across the endpoint so that it can hit the nearest CDN to get those images | A CDN puts copies of images and other static files closer to users. Imagine a shopper in India viewing a product image stored on a server in the US. A nearby CDN edge can serve that image faster and reduce work on the main server. I'd use cache headers and versioned image URLs so updates don't leave stale pictures forever. It's like placing popular products in local warehouses instead of shipping every request across the world. |


<a id="ia-18"></a>

## IA-18 — How would you autoscale services when traffic surges during holiday sales?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.87 | [58:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3529s) | 🟢 USEFUL | Autoscaling during sales spikes |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [59:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3540s) so generally uh we uh if you use the cloud service applications it also comes with something called alerting uh features it track the logs and uh we can have like some kind of like a threshold<br>[59:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3553s) so if it's exceeding our CPU utilize like more than this it automatically span the new uh I mean scan the servers or if it's get going below than that then it will also so like reduce the<br>[59:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3565s) number of instances of the servers so this help us to like orchestrate in a in a dynamic way rather than like hardcoding number of servers we want for the applications perfect sounds great | During a big sale, traffic doesn't stay the same all day. I configure autoscaling so the application adds instances when demand rises and removes them when it falls. For example, if checkout traffic doubles, we may need more checkout pods—but only if the database can keep up. I watch real indicators like request rate, latency, CPU and queue length, not CPU alone. Autoscaling is about maintaining a smooth customer experience, not just creating more servers. |


<a id="ia-19"></a>

## IA-19 — How would you implement infinite scroll with pagination, prefetching and loading feedback?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.88 | [59:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3592s) | 🟢 USEFUL | Backend and frontend pagination prompt |
| YT-1.89 | [1:00:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3628s) | 🟢 USEFUL | Lazy loading and infinite scrolling |
| YT-1.91 | [1:01:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3719s) | 🟢 USEFUL | Latency between scrolling and API response |
| YT-1.92 | [1:02:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3761s) | 🟢 USEFUL | Prefetching before viewport end |
| YT-1.93 | [1:03:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3786s) | 🟢 USEFUL | Skeleton states, debounce and throttle |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:00:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3602s) there is two different way one is like lazy loading of the data like we can load in<br>[1:00:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3616s) a bulk manner like first we load only like 100 then uh we keep on load other one is something called infinite scrolling uh which is like when you scroll upon the page whenever it hints<br>[1:00:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3628s) when the scroll hit the end of your viewport it will make a call to a database by sending the next page number to the back end so that our query will fetch the next 100 records starting from | I don't load 10,000 products into a browser at once. I load a small first page, then request the next set as the customer scrolls. I start the next request a little before the bottom so the page feels smooth, and I show a small loading placeholder if necessary. The API returns a stable page or cursor so items don't repeat. Great infinite scrolling should feel effortless because the work happens just ahead of the user. |


<a id="is-11"></a>

## IS-11 — How would you implement backend pagination using Spring Data JPA?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.90 | [1:01:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3678s) | 🟢 USEFUL | JPA pagination and batch fetching |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:01:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3692s) I think u i I'm not sure exactly with the query but I use the jpa uh methods which can uh which we can specify with our entity manager like what's the next uh next batch number and what could be<br>[1:01:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3707s) the size of the next batch | Pagination means asking the database for only the records we need right now. With Spring Data JPA, I can pass a Pageable such as PageRequest.of(0, 20) to get the first 20 products. The next request asks for the next page with a stable sort order. For an infinite-scroll screen, the frontend loads another page as the user moves down. I always cap page size; loading 20 useful records beats loading 20,000 at once. |


<a id="ic-1"></a>

## IC-1 — What Git branching and release promotion workflow have you used?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) we generally use the git for the versioning control and uh generally we have like a Dev branches and the QA and uh yeah generally we have like a master branch which is we also<br>[1:04:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3860s) called like a stable branch and for every monthly releases we create a new Branch from that it depends on how many what's the scale of our team so if there are many team members in the team so in<br>[1:04:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3872s) that case we also consider called a feature branch which uh so once the changes are done on the feature so we will do a kind of like a testing so this will get deployed on the testing | I like short-lived feature branches, pull requests, and one clear path to production. A developer finishes a change, automated tests run, teammates review it, and we build a versioned artifact. That same artifact moves through testing and staging before release. For example, if a release breaks checkout, we know exactly which version to roll back. Git branches organize work; tested builds and release gates make deployment dependable. |


<a id="ic-2"></a>

## IC-2 — How do feature branches progress through QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:04:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3894s) so once the qls also test we uh merge this to our a pre-pro branch it's not directly merch to the stable so<br>[1:05:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3905s) in the pre-pro branch we going to it looks like a same production Branch uh like it but customers are not using that uh changes this will just to ensure that our changes are working fine in the<br>[1:05:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3916s) customer environment once everything is looks fine then we deploy it on the production | I don't assume every environment needs its own Git branch. I build the application once, test it, and move the same version through QA, staging, and production. Each environment supplies its own configuration and secrets. For example, staging uses a test payment provider while production uses the real one, but the application code is the same. Promoting one known build is safer than rebuilding something slightly different at each stage. |


<a id="is-10"></a>

## IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.97 | [1:05:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3946s) | 🟢 USEFUL | Spring profiles with per-environment properties |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) it's generally called like profiling like uh generally we specify what kind of environment we are running so based on<br>[1:05:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3946s) that particular profile file uh if I just want to explain with the springboard uh we have application do uh application. property files generally that's like a default file we<br>[1:05:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3956s) use but we can also have something called application Dev application PR application staging So based on the environment these file will used and it will overhead the settings of the | I use Spring profiles so the same application can run with different settings. For example, development connects to a local database, while production uses its own database and credentials. I keep the common settings in application.yml and put environment differences in profile-specific files or external configuration. Then I activate the right profile during deployment. The idea is simple: one tested application, different environment settings—and no production passwords committed to Git. |


<a id="ic-3"></a>

## IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:06:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4005s) GitHub action or it could be junkins so generally it will uh check periodic changes are available so that's the reason we use like continuous inte Integrations and deployment continuous<br>[1:06:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4015s) deployment so this to ensure that uh every changes has to get deployed as soon as the new changes come into picture so it automatically see if there is any change in the commit IDs if it<br>[1:07:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4027s) figure it out then it automatically start to run the continuous to run the test cases then it will automatically deploy the changes | When a pull request is merged, GitHub Actions or Jenkins can start a pipeline from that push event. The pipeline checks out the commit, builds the code, runs tests, and publishes a versioned artifact. Depending on our release rules, it then deploys to staging or waits for production approval. For example, a failed security check should block deployment. A merge starts the process; passing the checks earns the release. |


<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |
| YT-1.100 | [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) | 🟢 USEFUL | Continuous integration checks |
| YT-1.101 | [1:08:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4122s) | 🟢 USEFUL | Continuous delivery and deployment |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) uh sure so as a name indicates CI is the continuous integration and uh continuous uh deliv deployments for the CD so when you see continuous integration means like uh generally I<br>[1:07:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4064s) write my code uh so that uh I mean I also write something called junit so that my codes are more uh unit test case based and U we could also follow some some tdd patterns so ensure that our<br>[1:07:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4075s) codes are more robust uh but once the changes is done we have to integrate with other component as well to find it whether it's working fine so that's where our CI come into picture so | CI means checking changes continuously so problems appear early. Every pull request can run a build, tests, and code checks. CD is what happens after that: continuous delivery keeps a tested release ready, while continuous deployment actually releases passing changes automatically. For example, a bank may require a human approval for production, even if its tests are green. I think of CI as 'Is it safe to merge?' and delivery as 'Is it ready to release?' |


<a id="ic-5"></a>

## IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.102 | [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | 🟢 USEFUL | Dockerfile, image and container |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) in our same project uh we can have something called docka files which have like bunch of instruction so it's could be like uh what could be the our jdk person and uh<br>[1:09:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4173s) I mean yeah what could be our entry point and what are the port should be enabled so these like a bunch of instruction helps the Dockers uh to uh in uh install these kind of packages and<br>[1:09:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4185s) uh uh execute the jar files okay so basically your Docker container that would have everything every Library everything that you need for your running on your instances now | A Dockerfile is a recipe for packaging my Java application. It tells Docker which runtime image to use, where to copy the JAR, and how to start it. For example, I can build a small Java 21 runtime image and run the same container locally or in the cloud. The image is the packaged recipe; the container is a running instance of it. I keep secrets outside the image and don't run as root unless necessary. |


<a id="ic-6"></a>

## IC-6 — How would you run and scale ten microservices with Kubernetes?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.103 | [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | 🟢 USEFUL | Managing multiple microservice containers |
| YT-1.104 | [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) | 🟢 USEFUL | Kubernetes orchestration and replicas |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) we use uh popularly kubernetes for the orchestration as a tool so generally this the job of the kubernetes is like scaling of these<br>[1:10:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4221s) containers so we can push or commit our uh images to our GitHub cloud and we can make it like very automated with our kubernetes so that whenever it sees like there is some over overhead in the<br>[1:10:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4235s) services it can create a new instance from our container so from our image sorry from the image it will create a new containers or if something is not getting used then it will can do the reverse way | Kubernetes helps me run many service containers without managing each one by hand. For example, I can tell it I want three order-service pods. If one dies, Kubernetes works to restore the desired number. A Service routes traffic to healthy pods, and autoscaling can add replicas when configured metrics say they're needed. It's useful, but it still needs proper health checks, limits, and monitoring. Kubernetes manages the desired state; I define what healthy looks like. |


<a id="ic-7"></a>

## IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.105 | [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | 🟢 USEFUL | Repeated Kubernetes pod crashes and CrashLoopBackOff scenario |
| YT-1.106 | [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) | 🟢 USEFUL | Crash triage, logs and PagerDuty |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:11:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4288s) so generally the developer will get pager Duty Call sometimes if if the periodic fail happens so we can still smart these alerts to think like<br>[1:11:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4303s) something which can control or something which we can't for example if something is a my scale is going down which is something which we can't control so that we can't do anything until the database<br>[1:11:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4313s) team has to fix but if server is going crash and our kubernetes is can't able to get it up the worst case is we have to manually bring this up uh but uh I I never encoun the case where uh we used | If a Kubernetes pod keeps crashing, I first find out why instead of restarting it repeatedly. I check the pod events, the previous container logs, and whether it ran out of memory, has bad configuration, or can't reach a dependency. For example, a missing environment variable can make every new pod fail immediately. If a new release caused it, I roll back and investigate. Restore the service first; fix the root cause next. |


<a id="ic-8"></a>

## IC-8 — How would you roll back a broken deployment to a previous container image?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.107 | [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | 🟢 USEFUL | Rollback to previous application version |
| YT-1.108 | [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) | 🟢 USEFUL | Release versioning and rollback workflow |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:12:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4379s) we also give something called versioning so it's like a name space followed by name and the version so it means like the kubernetes have the<br>[1:13:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4391s) versioning of our of the image so it means if last version is not working fine so it automatically goes to the previous one and create a new instance out of it so sorry new container out of<br>[1:13:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4402s) that image | I always keep a known-good application image so I can return to it after a bad release. If version 12 starts failing in production, I can roll back the Deployment to version 11 and check that requests recover. Kubernetes keeps rollout history when configured, but it doesn't automatically undo every failed release. I verify readiness, error rates, and customer impact after rollback. A rollback isn't finished when the command runs—it's finished when users are healthy again. |


<a id="ic-9"></a>

## IC-9 — What is infrastructure as code, and how would you use Pulumi for cloud alerts?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.109 | [1:14:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4453s) | 🟢 USEFUL | Infrastructure as code with Pulumi |
| YT-1.110 | [1:14:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4481s) | 🟢 USEFUL | Azure alerting and infrastructure automation |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:14:26](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4466s) I work with pumi which is like a terraform similar but yeah which can work as a infra as a service like where we can orchestrate the infrastructure<br>[1:14:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4481s) understood so uh what all infrastructures have you uh orchestrated with pulumi uh we uh I mean I worked with Azure so the b2c is the one like we use it very heavily for the authentications<br>[1:14:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4499s) and I really worked on the alert partings where uh we can trigger the alerts in a efficient way whenever something goes wrong so these two uh I worked and I made it bit automated with | Infrastructure as code means creating cloud resources from version-controlled definitions instead of clicking around manually. With Pulumi, I can describe Azure resources and alert rules using supported programming languages or YAML. For example, I can create an alert that notifies on-call engineers when checkout errors rise. The team reviews the changes before applying them, just like application code. If we can review and repeat it, infrastructure becomes easier to trust. |


<a id="it-1"></a>

## IT-1 — How should a team interpret a claim of 90 to 95 percent unit-test coverage?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.111 | [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | 🟢 USEFUL | High test coverage question |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) Okay so when we write the automations I generally concentrate on the unit test cases like every method should have its own test cases and I write with a junit f which supports<br>[1:16:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4593s) something called nested classes like uh so we can I can segregate the functionalities in the test cases and uh the mocking is something I use a lot because there are few things<br>[1:16:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4605s) when you're checking about the functionality you don't have to make a DB call every time in that case we can mock those calls and test the you can Mark what data you want to back and | 95% test coverage is a good number, but it doesn't mean our application is 95% bug-free. Coverage only tells us how much code our tests exercised. Imagine a payment service: testing successful payments isn't enough. We should also test failed payments and what happens when the bank doesn't respond. So I look at which important behaviors we test, not just the percentage. For me, good testing is about catching real problems, not chasing numbers. |


<a id="it-2"></a>

## IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.112 | [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | 🟢 USEFUL | JUnit tests and mocked dependencies |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4593s) the mocking is something I use a lot because there are few things<br>[1:16:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4605s) when you're checking about the functionality you don't have to make a DB call every time in that case we can mock those calls and test the you can Mark what data you want to back and<br>[1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) write your functionality for the test cases so that will increase my test cases I also use some code coverage tool and also sonar Cube U to do the static analysis of my code base to see what | I use JUnit to check what my service does and Mockito when I don't want to call a real database or API. For example, I can mock the repository to return one customer, call my service, and verify the result. Then I test what happens when the customer isn't found. Those are fast unit tests. Separate integration tests make sure the real database connection works. Mocking helps isolate the logic; integration tests make sure the pieces actually fit. |


<a id="it-3"></a>

## IT-3 — How is SonarQube used for static analysis and code quality checks?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.113 | [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) | 🟢 USEFUL | SonarQube and static analysis |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) I also use some code coverage tool and also sonar Cube U to do the static analysis of my code base to see what<br>[1:17:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4628s) could be the uh what are could be the some technical Dev not technical Dev like some technical issues which can be fixed and you have done that in local configured that as a<br>[1:17:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4640s) plugin uh yes uh it just we how to write uh I I did that for the Android project not for the uh spring board one but it's pretty same I think uh we just have to uh mention a few of the properties in | SonarQube helps the team spot code-quality and security issues early. For example, it may flag a risky coding pattern or a piece of duplicated code in a pull request. Our CI pipeline sends the code and relevant test-coverage reports to SonarQube, and a quality gate can flag or block the change. But SonarQube can't prove the application works correctly. It's a useful second pair of eyes, not a replacement for good tests. |


<a id="it-4"></a>

## IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.114 | [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | 🟢 USEFUL | Do not test trivial getters just for coverage |
| YT-1.115 | [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) | 🟢 USEFUL | Exclude DTO boilerplate from coverage |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) we can write like a rejects patterns which can uh exclude these kind of<br>[1:18:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4739s) packages which we don't want to track in our coveres so uh we uh I mean have written in XML with mavin like we can specify like what kind of packages you can use like dot star for the dtos like<br>[1:19:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4754s) generally we follow the vering sorry package patterns for all the files like some dto should go under dto package and entity should go so these Getters and Setters pojo files uh we don't have to | I don't write tests for trivial getters just to make the coverage number look impressive. I spend that time on validation, calculations, and failure handling—places where bugs hurt customers. For example, a DTO getter usually needs no special test, but a custom JSON mapping or validation rule might. If generated boilerplate should be excluded, I configure and explain that in the coverage tool. The goal is honest coverage that reflects valuable tests. |


<a id="it-5"></a>

## IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.116 | [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | 🟢 USEFUL | Integration tests for entities and services |
| YT-1.117 | [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) | 🟢 USEFUL | Microservice end-to-end testing |
| YT-1.118 | [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) | 🟢 USEFUL | Avoid real cross-service calls in unit tests |
| YT-1.119 | [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) | 🟢 USEFUL | Use separate integration/system-test suites |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:20:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4816s) I have written the test cases but generally it's more like a integration test case only where<br>[1:20:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4827s) we make the call to the uh rest template uh with by passing the payload so so one way we have to ensure like these uh services are running and also like the for this particular request the<br>[1:20:40](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4840s) corresponding response is coming back or not so we don't have to test cases itself you have involved this particular part yes uh because like even when we make a call to different micros service | I keep three levels of testing separate. Unit tests check one service's logic quickly, using mocks for outside calls. Integration tests check real pieces working together, like a repository with a test database. A smaller end-to-end suite checks the full journey—for example, cart to order to payment—in a test environment. If every unit test calls ten live services, builds become slow and unreliable. Test small things quickly and complete journeys deliberately. |


<a id="is-12"></a>

## IS-12 — What is reactive programming in Spring WebFlux, and how do Mono and Flux differ?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.120 | [1:22:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4951s) | 🟡 INTRO | Introduction to reactive Spring applications |
| YT-1.121 | [1:22:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4966s) | 🟢 USEFUL | Blocking versus nonblocking I/O |
| YT-1.122 | [1:23:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5013s) | 🟢 USEFUL | Mono and Flux overview |
| YT-1.123 | [1:23:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5032s) | 🟢 USEFUL | Project Reactor in Spring |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:22:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4966s) uh so generally we go with the reactive programming because the threats are<br>[1:22:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4977s) limited like uh so we can't have like threads waiting for the response to come back so when we write any calls these are like as synchronous calls like because few of the operation has to be<br>[1:23:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4989s) done one after the other so in that case we block the threats to wait for the response to come back so in that case uh we can go with a reactive programming where uh something called like a call | Reactive programming is useful when an application spends a lot of time waiting for network or database responses. Instead of tying up one thread while it waits, nonblocking code can let that thread handle other work. In Spring WebFlux, Mono represents zero or one result, while Flux can represent many. Imagine a service receiving thousands of slow API responses: this can improve resource use. Reactive isn't automatically faster for every task, especially if the code still blocks. |


<a id="ic-10"></a>

## IC-10 — Compare Maven and Gradle as Java build tools.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.124 | [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) | 🟢 USEFUL | Maven versus Gradle question |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:24:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5071s) these are called like a different way of uh writing the build build files so one is the build tools not build file build<br>[1:24:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5086s) tools uh so when we generally I think all of you all of us like familiar with the mavin which we can easily see with pal. XML the gradal is also something which does similar uh we can see that<br>[1:24:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5097s) whenever we use any uh packages we whenever we stck it in an mvn repository there are different flavors available one is mavin other one is Gradle so Gradle is like there is it's naming | Maven and Gradle solve the same big problem: building a Java project without manually managing every dependency and command. Maven usually uses pom.xml and a familiar lifecycle. Gradle uses a task-based build with Groovy or Kotlin scripts and can make strong use of caching. For example, both can run tests and produce the same Spring Boot JAR. I choose based on the team's build needs and consistency, not on a claim that one is always faster. |


<a id="ic-11"></a>

## IC-11 — What is the purpose of pom.xml and how does Maven resolve dependencies?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.125 | [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) | 🟢 USEFUL | Interview question switches to why pom.xml is used |
| YT-1.126 | [1:25:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5136s) | 🟢 USEFUL | Purpose of pom.xml |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:25:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5120s) the main problem if you don't use pom is like uh if you want<br>[1:25:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5136s) to enhance our uh jar files to the next uh I mean next versing so the thing is like I have to do manually uh that's the main problem like I have to install the new version put it in the respective<br>[1:25:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5148s) folder so that my code will be running as is it and another problem is like if I'm giving my project to someone else and the other user doesn't have the required | pom.xml is the instruction sheet for a Maven project. It says which dependencies we need, which versions or version rules apply, and how to build the application. For example, when I add the PostgreSQL driver, Maven checks its local cache and downloads the dependency from a configured repository if necessary. Another developer can build the same project without manually hunting for JAR files. The POM makes the build repeatable and understandable. |


<a id="ic-12"></a>

## IC-12 — Compare Kanban and Scrum and explain how they affect a team's delivery workflow.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.127 | [1:26:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5212s) | 🟢 USEFUL | Kanban versus Scrum in team workflow |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:27:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5252s) I haven't uh worked in any team which uses can ban but sometimes the team uses mix of like can ban and also like uh uh scrum so<br>[1:27:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5267s) yeah I uh I mean I work mainly in the scrum and the iel methodology IES and that's written in a resume you can be hit up on this oh okay I I did not check that no worries no worries just have a<br>[1:28:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5282s) look with the SK band thing written in this I think this is more of the uh strict way of following the uh Sprint work as far as I understand okay um um so the next thing I would have asked you | Scrum and Kanban are two ways of keeping work visible and moving. Scrum plans work in timeboxed sprints, with review and planning routines. Kanban uses a flow board and limits work in progress, so the team finishes tasks before starting too many new ones. For example, a support team dealing with unpredictable incidents may prefer Kanban, while a product team may use Scrum. The best method helps the team deliver, not just attend meetings. |


<a id="ij-1"></a>

## IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.128 | [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | 🟢 USEFUL | ConcurrentHashMap internal design question |
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |
| YT-1.131 | [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) | 🟢 USEFUL | Legacy segment-lock explanation caveat |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) with the regular hashmap what we use is is something called like a a fail fast<br>[1:28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5317s) sorry it's a fail first uh hashing it means what like whenever uh we are iterating on this hash map and concurrently if something is going change in this hash let's say like we're<br>[1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) adding new entries so it will throw an exception because it the uh the way it works in a different because it keep on check the hash size if something is getting changed it will throw the | HashMap works well when one thread controls the data, but it isn't safe for unsynchronized concurrent updates. ConcurrentHashMap is built for multiple threads reading and updating the map together. For example, several requests may update different entries in a shared counter map. It offers operations such as compute that help update values safely, and its iterators can tolerate changes. It doesn't make every multi-step business operation atomic, so I still choose the right operation. |


<a id="ij-3"></a>

## IJ-3 — How does HashMap fail-fast iteration compare with ConcurrentHashMap iteration?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:28:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5336s) exception called concurrent hash exception to avoid this kind of like uh scenario we can go with like a new family of the uh hashing is called concurrent hashmap so it will works in<br>[1:29:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5350s) efficient way so that even if you do add any entities to the hashmap while you are iterating so it will be uh efficient to handle that kind of scenarios so that will be very useful when we have a yeah<br>[1:29:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5362s) exception will be uh I don't think any exception will come because this is kind of like a main uh uh hashing we use especially for the multi- thread environments when there are more than | A HashMap iterator usually notices structural changes and may throw ConcurrentModificationException, but that fail-fast behavior is only a best-effort warning. It isn't thread safety. ConcurrentHashMap uses weakly consistent iteration: another thread can update the map while I'm looping, without that exception, but I may not see a perfect snapshot. For example, a live metrics dashboard can often tolerate that. If I need an exact snapshot, I must coordinate it explicitly. |


<a id="ij-2"></a>

## IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.132 | [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | 🟢 USEFUL | Using employee objects as HashMap keys |
| YT-1.133 | [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) | 🟢 USEFUL | equals and hashCode contract |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) if you want to make any object as the key uh the two things we have to override one is the<br>[1:31:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5497s) equal method and other one is uh hash code so the main reason is like even though uh we have to ensure that whether these two object are same or not it can be easily distinguished based on these<br>[1:31:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5509s) two methods so whenever uh when we we do any put it will automatically call these methods and get to ensure that whether it is a update to the same object or it is a new insert So based on the | If I use Employee objects as HashMap keys, Java needs to know when two Employee objects represent the same key. That's why I implement equals and hashCode consistently. For example, two objects with the same immutable employee ID should normally compare equal and return the same hash code. If the ID changes after insertion, lookup may break. The simple rule is: equal keys need equal hash codes, and keys should stay stable in the map. |


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
