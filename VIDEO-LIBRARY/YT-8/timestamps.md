# YT-8 — Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode

**Video:** https://www.youtube.com/watch?v=PHIQJeKzMCU · **27 distinct interview questions** · **61 curated timestamp sections**.

[Pure video chronological timeline](timeline.md) · [Unedited full linked transcript](transcript.md) · [Coverage audit](coverage-audit.md)

⭐ means this interview question already exists elsewhere in the library, so its permanent ID is reused.

## Find a question

| Watch | Question |
|---|---|
| [1:34](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=94s) | [IS-14 — What are Spring Boot Actuator health and metrics endpoints used for?](#is-14) ⭐ |
| [3:08](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=188s) | [IS-34 — How can an application expose Actuator on a different management port?](#is-34) |
| [4:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=263s) | [IS-35 — When is Spring AOP useful and how is it different from ControllerAdvice?](#is-35) |
| [5:17](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=317s) | [IS-32 — How do @ControllerAdvice and @ExceptionHandler work?](#is-32) ⭐ |
| [7:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=466s) | [IA-11 — How should cart, product, inventory and user responsibilities be split across services?](#ia-11) ⭐ |
| [9:54](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=594s) | [IA-18 — How would you autoscale services when traffic surges during holiday sales?](#ia-18) ⭐ |
| [11:30](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=690s) | [IA-83 — What does a circuit breaker and fallback do when a service fails?](#ia-83) |
| [12:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=760s) | [IA-21 — How would backend microservices communicate with each other using HTTP clients?](#ia-21) ⭐ |
| [14:00](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=840s) | [IA-84 — How do OpenFeign and RestTemplate differ?](#ia-84) |
| [15:15](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=915s) | [ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?](#id-3) ⭐ |
| [16:37](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=997s) | [IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.](#ia-5) ⭐ |
| [18:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1109s) | [IS-36 — What roles do an authorization server and resource server play?](#is-36) |
| [20:14](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1214s) | [IC-1 — What Git branching and release promotion workflow have you used?](#ic-1) ⭐ |
| [23:14](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1394s) | [IS-19 — How does Spring Cloud Config share configuration among microservices?](#is-19) ⭐ |
| [24:13](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1453s) | [IC-24 — What should you review in a teammate's pull request?](#ic-24) |
| [26:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1570s) | [IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?](#it-2) ⭐ |
| [28:56](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1736s) | [IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?](#ic-5) ⭐ |
| [31:18](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1878s) | [IC-6 — How would you run and scale ten microservices with Kubernetes?](#ic-6) ⭐ |
| [33:01](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1981s) | [IC-16 — Why publish Docker images to a container registry?](#ic-16) ⭐ |
| [34:26](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2066s) | [IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.](#ic-4) ⭐ |
| [35:18](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2118s) | [IC-25 — What is infrastructure as code with Terraform?](#ic-25) |
| [36:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2164s) | [IA-40 — When would you choose Factory, Singleton, or Builder patterns?](#ia-40) ⭐ |
| [37:42](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2262s) | [IA-34 — What does the SOLID single-responsibility principle mean?](#ia-34) ⭐ |
| [39:02](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2342s) | [IC-19 — How do trace IDs and span IDs help debug distributed calls?](#ic-19) ⭐ |
| [40:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2440s) | [IC-20 — How would you send production alerts using AWS CloudWatch?](#ic-20) ⭐ |
| [43:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2590s) | [IA-85 — When is asynchronous messaging better than a direct REST call?](#ia-85) |
| [48:12](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2892s) | [IS-37 — How can Spring AOP record method entry and exit automatically?](#is-37) |

## Non-question source context — intros, promotions and closing

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.1 | [0:00](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=0s) | 🟡 INTRO | Interview introduction and candidate background |
| YT-8.58 | [56:16](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3376s) | 🔴 NO NEED | Interview feedback and closing |
| YT-8.59 | [57:21](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3441s) | 🔴 NO NEED | Interview feedback and closing |
| YT-8.60 | [58:36](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3516s) | 🔴 NO NEED | Interview feedback and closing |
| YT-8.61 | [59:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3550s) | 🔴 NO NEED | End of interview or closing remarks |

<a id="is-14"></a>

## IS-14 — What are Spring Boot Actuator health and metrics endpoints used for? ⭐

⭐ **Repeated interview question:** reused **IS-14**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.2 | [1:34](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=94s) | 🟢 USEFUL | What does Spring Boot Actuator expose and how do you secure it? |
| YT-8.3 | [2:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=160s) | 🟢 USEFUL | Follow-up: What does Spring Boot Actuator expose and how do you secure it? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=106s) actuator anywhere in the project yes I have used actuators yeah yeah so uh yeah so yeah so actuators allows us to know insights of of the pro project or the service that we are we are developing so<br>[2:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=124s) um if you want to make a use of actuator so we have to add the one dependency spring boot starter actuator after adding that dependency there is some configuration that we have to mention in | Actuator offers management information such as health, metrics, and application details when enabled and exposed. For example, a readiness endpoint helps a load balancer avoid an unavailable pod. I explicitly choose which endpoints are exposed and protect sensitive management information. A management port can also be configured separately. |

<a id="is-34"></a>

## IS-34 — How can an application expose Actuator on a different management port?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.4 | [3:08](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=188s) | 🟢 USEFUL | How can an application expose Actuator on a different management port? |
| YT-8.49 | [46:48](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2808s) | 🟢 USEFUL | Why configure Spring Boot management endpoints separately from the main API? |
| YT-8.50 | [47:58](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2878s) | 🟢 USEFUL | Follow-up: Why configure Spring Boot management endpoints separately from the main API? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [3:20](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=200s) endpoint so that's what you configure in properties so how do you change it and uh how what if I don't want to have it on a default okay so uh default Port means you are<br>[3:34](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=214s) asking about that server. Port uh we can server Port Port is the port for the application uh application yes uh is the server port and the management Ino port for the actuator | Spring Boot can use management.server.port to expose management HTTP endpoints on a separate port. For example, application traffic can use 8080 while Actuator is bound to a restricted management network. I also configure management endpoint exposure and authorization. Changing server.port alone changes the main application port, not necessarily a separate management interface. |

<a id="is-35"></a>

## IS-35 — When is Spring AOP useful and how is it different from ControllerAdvice?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.5 | [4:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=263s) | 🟢 USEFUL | When is Spring AOP useful and how is it different from ControllerAdvice? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [4:37](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=277s) aop um yeah in case of uh exceptional handling uh if you want to handle the exception in our uh spring boot uh or microservices API so in that case generally when we are creating that<br>[4:50](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=290s) Global exception Handler in that case internally the aop is being used um but uh yeah so whenever we are throwing exception that the control is coming to our Global exception Handler | Spring AOP applies cross-cutting behavior at method join points through proxies, such as timing or audit logging. @ControllerAdvice provides centralized web exception handling and is not simply a general AOP advice. For example, I can log service method duration with @Around and map an OrderNotFoundException to HTTP 404 with @ExceptionHandler. |

<a id="is-32"></a>

## IS-32 — How do @ControllerAdvice and @ExceptionHandler work? ⭐

⭐ **Repeated interview question:** reused **IS-32**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.6 | [5:17](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=317s) | 🟢 USEFUL | How do you handle application exceptions centrally in Spring Boot? |
| YT-8.7 | [6:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=383s) | 🟢 USEFUL | Follow-up: How do you handle application exceptions centrally in Spring Boot? |
| YT-8.8 | [7:30](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=450s) | 🟢 USEFUL | Follow-up: How do you handle application exceptions centrally in Spring Boot? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [5:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=329s) have creating a global exception Handler class firstly we Mark our class as at R controller advice on the top of the class then um after that we are creating one method on the top of that method we<br>[5:43](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=343s) are uh marking that method with at exceptional Handler annotations with the type of exception that we want to throw let's say I want to throw the exception for order not found exception so we will | I use @RestControllerAdvice with @ExceptionHandler methods to translate expected exceptions into HTTP responses. For example, a missing order can become 404 with a clear error body, while an unexpected error should become a safe 500 response and be logged. The business layer still throws meaningful exceptions where appropriate. |

<a id="ia-11"></a>

## IA-11 — How should cart, product, inventory and user responsibilities be split across services? ⭐

⭐ **Repeated interview question:** reused **IA-11**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.9 | [7:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=466s) | 🟢 USEFUL | How do you split an e-commerce monolith into business microservices? |
| YT-8.10 | [8:54](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=534s) | 🟢 USEFUL | Follow-up: How do you split an e-commerce monolith into business microservices? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [8:08](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=488s) many micros Services you can think about it that's what I'm expecting from okay yeah uh so um in this case we will divide this uh micros service into microservices such as based on the<br>[8:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=503s) functionality so first will be like uh uh search so so whatever the search part is there in in that monic application so that we will take as a one service searching searching and filtering | I divide services around cohesive business capabilities rather than arbitrary technical layers. For example, catalog, ordering, payments, inventory, and delivery can own different rules and data. I first define the boundaries and communication between them, because splitting too early can create unnecessary distributed complexity. |

<a id="ia-18"></a>

## IA-18 — How would you autoscale services when traffic surges during holiday sales? ⭐

⭐ **Repeated interview question:** reused **IA-18**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.11 | [9:54](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=594s) | 🟢 USEFUL | How would you scale one heavily used microservice during a sale? |
| YT-8.12 | [11:09](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=669s) | 🟢 USEFUL | Follow-up: How would you scale one heavily used microservice during a sale? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [10:21](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=621s) spin up the instances we can have the uh uh scale of horizontal scaling suppose um the average TPS transaction per second is suppose 10 now they are suddenly 15 or 20 then we will uh spin<br>[10:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=640s) up the instances uh that are deployed on on onto the cloud so this way also um Suppose there is a one functionality that is used frequently uh let's say the search functionality compared to other | I measure traffic and bottlenecks, then scale only the service that needs more capacity. For example, product search may need more replicas than checkout during browsing-heavy traffic. Horizontal scaling helps stateless APIs, but I still check database limits and caching. Scaling every service blindly wastes resources. |

<a id="ia-83"></a>

## IA-83 — What does a circuit breaker and fallback do when a service fails?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.13 | [11:30](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=690s) | 🟢 USEFUL | What does a circuit breaker and fallback do when a service fails? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [11:43](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=703s) pattern uh for that uh uh that we can Implement with the resilence 4J that is the uh new implementation thing previously it was histric um so we can we can write one uh<br>[11:58](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=718s) method I think it is called as fallback method so whatever the uh default response that for time being that can be shown to the user user friendly message okay yeah or some list of products for | A circuit breaker stops repeatedly calling an unhealthy dependency after failures exceed a configured threshold. For example, if recommendations are down, a shopping page can show a safe default instead of waiting through repeated timeouts. Fallbacks must be meaningful; they cannot pretend a failed payment succeeded. |

<a id="ia-21"></a>

## IA-21 — How would backend microservices communicate with each other using HTTP clients? ⭐

⭐ **Repeated interview question:** reused **IA-21**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.14 | [12:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=760s) | 🟢 USEFUL | How do Feign clients and load balancing work together? |
| YT-8.15 | [13:45](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=825s) | 🟢 USEFUL | Follow-up: How do Feign clients and load balancing work together? |
| YT-8.45 | [41:54](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2514s) | 🟢 USEFUL | How should two microservices communicate synchronously? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [12:54](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=774s) balancing in a round robin fashion so we will be having the G Gateway we will be set up gateway then uh urea server and the fin client so the the communication between<br>[13:06](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=786s) Services uh we can do with the help of your server fin client so fin Cent internally uses the load balancing client side load balancing so Suppose there are three services so first time | A declarative Feign client defines an HTTP service contract, while a load-balancing mechanism can select among discovered service instances. For example, OrderService calls inventory by service name without hardcoding pod addresses. Feign is an HTTP client abstraction; it does not guarantee round-robin or resilience without configuration. |

<a id="ia-84"></a>

## IA-84 — How do OpenFeign and RestTemplate differ?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.16 | [14:00](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=840s) | 🟢 USEFUL | How do OpenFeign and RestTemplate differ? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:13](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=853s) case of rest template we have to Auto at rest template and based on our type um we have to mention the URL as well as the uh the parameter in the map or the path variable that we have to mention<br>[14:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=869s) okay but yeah I don't know the exactly no no understood U okay so in any ways fake line you find better than rest template in any scenario uh I think there generally their main uses is like service to | OpenFeign defines an HTTP interface that Spring integrates with configuration, while RestTemplate is an imperative client where code builds requests directly. For example, a typed InventoryClient interface is convenient for repeated internal calls. Both can call internal or external APIs. Modern Spring applications may also consider RestClient or WebClient. |

<a id="id-3"></a>

## ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data? ⭐

⭐ **Repeated interview question:** reused **ID-3**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.17 | [15:15](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=915s) | 🟢 USEFUL | How do database-per-service and shared databases compare? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:38](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=938s) micros Services yeah um I will use um based on the requirement uh we can use the database we can have multiple database also um so like for search related thing<br>[15:53](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=953s) we can use the mongodb kind of thing and for other think we can use the um rdbms also we can use I mean when will you use noq when will you use my SQ um for uh search related means | A database-per-service design gives each service ownership of its data schema and migrations. For example, payments and catalog can evolve independently. A shared database can simplify transactions initially but creates tight coupling. I choose SQL or NoSQL based on each service's access patterns and consistency requirements, not the microservice label alone. |

<a id="ia-5"></a>

## IA-5 — Compare Saga and two-phase commit for distributed microservice transactions. ⭐

⭐ **Repeated interview question:** reused **IA-5**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.18 | [16:37](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=997s) | 🟢 USEFUL | How do you handle a payment failure across several microservices? |
| YT-8.19 | [17:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1066s) | 🟢 USEFUL | Follow-up: How do you handle a payment failure across several microservices? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:49](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1009s) the products added to the card placed an order did the payment the delivery partner is assigned I'm waiting for my order what happens if uh my payment is failed then I have to<br>[17:02](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1022s) roll back it up completely so how will you manage this yeah uh we can manage this by using distributed uh transaction uh by making use of The Saga design pattern okay and what is Saga design | A distributed workflow can use a Saga with compensating actions. For example, an order reserves stock, payment fails, and a compensation releases stock and marks the order failed. Unlike one database rollback, these actions happen in separate local transactions. I include idempotency and retries because partial failures are expected. |

<a id="is-36"></a>

## IS-36 — What roles do an authorization server and resource server play?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.20 | [18:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1109s) | 🟢 USEFUL | What roles do an authorization server and resource server play? |
| YT-8.21 | [19:43](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1183s) | 🟢 USEFUL | Follow-up: What roles do an authorization server and resource server play? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [18:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1126s) securing the end points that are being exposed or used by the other services so we we we can add uh uh security by configuring the o by making use of the some kind of<br>[19:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1144s) token for that I think we need resource server and uh authorization server so I think resource resource server is creating the token and uh other server one one server | An authorization server authenticates or authorizes a client and issues access tokens. A resource server hosts the protected API and validates those tokens. For example, a Spring order API checks a JWT issued by a trusted identity provider. The issuer creates the token; the API does not normally invent a new token for every request. |

<a id="ic-1"></a>

## IC-1 — What Git branching and release promotion workflow have you used? ⭐

⭐ **Repeated interview question:** reused **IC-1**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.22 | [20:14](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1214s) | 🟢 USEFUL | How do pull requests and release branches support teamwork? |
| YT-8.23 | [21:19](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1279s) | 🟢 USEFUL | Follow-up: How do pull requests and release branches support teamwork? |
| YT-8.24 | [22:33](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1353s) | 🟢 USEFUL | Follow-up: How do pull requests and release branches support teamwork? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [20:38](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1238s) raising the pool request PR we call it as okay so yeah so in that case whenever he is raising the pr firstly he is getting the pool and suppose some developer is also working on the same<br>[20:52](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1252s) file then he will get the conflict so he will resolve those conflict or he will take other Stranges and then he will pull and once we raise the pull request we ask for the code review the architect | Developers work in focused branches, open pull requests, get reviews, and merge after required checks pass. For example, a small inventory change can move through development and QA before production. I keep a clear release history and avoid bypassing branch protections just to ship faster. |

<a id="is-19"></a>

## IS-19 — How does Spring Cloud Config share configuration among microservices? ⭐

⭐ **Repeated interview question:** reused **IS-19**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.25 | [23:14](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1394s) | 🟢 USEFUL | Where should common microservice configuration live? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [23:30](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1410s) in in the same microservice in in the microservice itself so all microservices will have the same properties that's her yeah okay and I have 100 properties and 100 all the 100 properties for all<br>[23:45](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1425s) the microservices are common then you will duplicate the code 100 time 100 time 100 100 for each micros service that's some so I think as per my understanding for uh | Common nonsecret configuration can be managed centrally using Spring Cloud Config or deployment configuration. For example, several services can share tracing endpoints while each has its own database settings. I avoid copying the same settings across dozens of projects. Secrets need a secure manager and controlled access. |

<a id="ic-24"></a>

## IC-24 — What should you review in a teammate's pull request?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.26 | [24:13](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1453s) | 🟢 USEFUL | What should you review in a teammate's pull request? |
| YT-8.27 | [25:26](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1526s) | 🟢 USEFUL | Follow-up: What should you review in a teammate's pull request? |
| YT-8.54 | [51:27](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3087s) | 🟢 USEFUL | What is an effective code-review checklist for a senior Java developer? |
| YT-8.55 | [52:35](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3155s) | 🟢 USEFUL | Follow-up: What is an effective code-review checklist for a senior Java developer? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [24:27](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1467s) have the proper PR review done for my Cod base yeah firstly it should be a compile then um but that will Beck Jin only right yeah yeah yes yeah oh correct unit test cases should be there but that<br>[24:42](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1482s) is also done by Jenkins yeah and uh then comments should be there which are the methods that has been added comment should be added but from this yeah these are the | I check business behavior, edge cases, security, naming, tests, data access, and unintended side effects. For example, a new order query may work in tests but be missing an index for production traffic. CI handles mechanical checks, while human review focuses on design and correctness. Comments should be concrete and useful. |

<a id="it-2"></a>

## IT-2 — How do JUnit tests and mocks isolate logic from databases and other services? ⭐

⭐ **Repeated interview question:** reused **IT-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.28 | [26:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1570s) | 🟢 USEFUL | How do unit tests, integration tests, and Mockito relate? |
| YT-8.29 | [27:22](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1642s) | 🟢 USEFUL | Follow-up: How do unit tests, integration tests, and Mockito relate? |
| YT-8.30 | [28:41](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1721s) | 🟢 USEFUL | Follow-up: How do unit tests, integration tests, and Mockito relate? |
| YT-8.56 | [53:52](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3232s) | 🟢 USEFUL | Why mock database or network calls in unit tests? |
| YT-8.57 | [55:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3304s) | 🟢 USEFUL | Follow-up: Why mock database or network calls in unit tests? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:27](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1587s) manually means once the code is getting deployed and all other components are getting communicate so one one kind of sity before hand overing it to the testers soting yes any knowledge about the<br>[26:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1606s) bdds or test yeah that uh uh I I don't much work on that but yes I have that uh understanding about the um test driven development dddd so writing the scenarios into that uh that file by when | Unit tests isolate one component and mock its dependencies, while integration tests exercise real boundaries such as repositories and external services. Mockito lets me control collaborators without hitting a real database. For example, I test discount rules using a mocked repository, then verify SQL mappings separately in an integration test. |

<a id="ic-5"></a>

## IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application? ⭐

⭐ **Repeated interview question:** reused **IC-5**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.31 | [28:56](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1736s) | 🟢 USEFUL | Why do teams containerize Java services with Docker? |
| YT-8.32 | [30:09](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1809s) | 🟢 USEFUL | Follow-up: Why do teams containerize Java services with Docker? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [29:13](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1753s) uh in case of Docker means we can we can deploy our services uh nicely so uh if you want to doize any application so it uses a very lightweight bootstrap OS to deploy the<br>[29:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1769s) services so there is one problem we used to get previously like here it is working in one environment it is working or on on my local is working and some at others locals it is not working so with | Docker packages an application with a controlled runtime and dependencies into an image. For example, the same Spring Boot image can be run in development and production with different external configuration. This reduces environment differences. An image is immutable; running containers are instances created from it. |

<a id="ic-6"></a>

## IC-6 — How would you run and scale ten microservices with Kubernetes? ⭐

⭐ **Repeated interview question:** reused **IC-6**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.33 | [31:18](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1878s) | 🟢 USEFUL | How does Kubernetes manage Docker-compatible containers? |
| YT-8.34 | [32:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1960s) | 🟢 USEFUL | Follow-up: How does Kubernetes manage Docker-compatible containers? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:35](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1895s) and whatever the our project code libraries and everything Java Java version whichever we want jdk same same jdk okay okay um and you when when you have multiple containers with all the<br>[31:55](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1915s) microsof you have n number of containers created right one container having this one having another micros service another container you have suppose you have 100 microservices working 100 | Kubernetes schedules application pods, manages desired replica counts, and replaces failed pods according to configuration. For example, a Deployment declares three replicas for the catalog service. Kubernetes uses OCI-compatible images and does not require Docker as the node runtime. Its main job is to reconcile desired and observed state. |

<a id="ic-16"></a>

## IC-16 — Why publish Docker images to a container registry? ⭐

⭐ **Repeated interview question:** reused **IC-16**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.35 | [33:01](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1981s) | 🟢 USEFUL | How do image tags and registries support reproducible releases? |
| YT-8.36 | [34:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2050s) | 🟢 USEFUL | Follow-up: How do image tags and registries support reproducible releases? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [33:20](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2000s) container the registry is there I don't remember exact name container registry container regist okay okay and how do you maintain the versioning of your Docker images versioning for Docker<br>[33:33](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2013s) images yes the version of the application of the jar the jar version so every time you deploy you increase your jar version that's how with every deployment yes okay | A container registry stores built images identified by tags and digests. For example, an image built from one Git commit can be deployed and rolled back consistently. I prefer immutable version tags or digest pinning rather than relying on latest. That links a release to the actual artifact tested. |

<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates. ⭐

⭐ **Repeated interview question:** reused **IC-4**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.37 | [34:26](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2066s) | 🟢 USEFUL | What stages belong in a Jenkins deployment pipeline? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:41](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2081s) flow yeah so um there are various jobs configured build build is there then some uh security uh means in in in my current project 45 is uh 45 is configur to check some security related things<br>[34:59](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2099s) then um deploying to the cloud for that um terraforms files are written in our project for each of the environment those file are read and the services getting deployed into the ECS elastic container | A typical Jenkins pipeline checks out code, compiles it, runs tests and scans, packages the artifact, builds an image, and promotes the release after approval or gates. For example, a failing code-quality check should prevent production deployment. I publish build results so the team knows exactly what was released. |

<a id="ic-25"></a>

## IC-25 — What is infrastructure as code with Terraform?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.38 | [35:18](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2118s) | 🟢 USEFUL | What is infrastructure as code with Terraform? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:34](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2134s) minimum in minimum memory or instances then uh account number so all these steps are mention inside the terraform file and it is created for each environment so basically helping for the<br>[35:49](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2149s) deployment to genkins okay okay and the genkins build pipeline you have just a security check a build check any sonar checks anything yes yes they are also there yeah J units and the sonar cubes | Terraform describes cloud infrastructure in configuration files and applies a reviewed plan to create or change resources. For example, it can declare a load balancer and security groups instead of requiring manual console clicks. State management and approvals matter. Infrastructure as code makes changes repeatable and reviewable. |

<a id="ia-40"></a>

## IA-40 — When would you choose Factory, Singleton, or Builder patterns? ⭐

⭐ **Repeated interview question:** reused **IA-40**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.39 | [36:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2164s) | 🟢 USEFUL | How do Builder and Singleton patterns solve different problems? |
| YT-8.40 | [37:09](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2229s) | 🟢 USEFUL | Follow-up: How do Builder and Singleton patterns solve different problems? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [36:21](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2181s) also I have used why Singleton where have you used Singleton design patter why have you used the use case for the single T is like uh in case of logging you can we can<br>[36:36](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2196s) have means driver objects loading logging okay as well as uh there we can use the single okay okay okay and where have you used the Builder on any scenario you yeah so I have a class with lot of | Builder makes construction readable for an object with many optional properties, while Singleton controls how many instances exist in a scope. For example, a ReportBuilder assembles a report; a shared configuration object might have singleton lifetime. I choose a pattern for its actual purpose rather than combine them by default. |

<a id="ia-34"></a>

## IA-34 — What does the SOLID single-responsibility principle mean? ⭐

⭐ **Repeated interview question:** reused **IA-34**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.41 | [37:42](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2262s) | 🟢 USEFUL | Why is single responsibility important for service design? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [38:01](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2281s) project single responsibility um uh for for one service there should be uh one and only one functionality that should be done by that service suppose we are having one<br>[38:15](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2295s) functional yeah so we should Implement only we should not mix multiple functionality into the one service suppose I'm doing some arithmetic operation so then addition | A service should own one coherent business capability or reason to change. For example, catalog should not also implement payment settlement and shipping assignment. Clear responsibilities help deployment and testing, although operations often span multiple services. The important thing is a boundary that matches business ownership. |

<a id="ic-19"></a>

## IC-19 — How do trace IDs and span IDs help debug distributed calls? ⭐

⭐ **Repeated interview question:** reused **IC-19**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.42 | [39:02](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2342s) | 🟢 USEFUL | How would you correlate logs across a distributed request? |
| YT-8.43 | [40:12](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2412s) | 🟢 USEFUL | Follow-up: How would you correlate logs across a distributed request? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [39:15](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2355s) we have they are producing the logs so those logs are Gather in the kibana and if suppose we want to troubleshoot if there is any issue then we can search by using that application name and that<br>[39:29](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2369s) particular log or some unique ID to know if there is any issue for that purpose we are using kibana okay and who consolidates all those logs and give it to kibana in this case uh I don't know | I propagate a trace ID or correlation ID through incoming requests and downstream calls. For example, an order request touching cart, payment, and inventory should be searchable under one trace. Each step can have its own span. Centralized logs and tracing tell a clearer story than scattered timestamps alone. |

<a id="ic-20"></a>

## IC-20 — How would you send production alerts using AWS CloudWatch? ⭐

⭐ **Repeated interview question:** reused **IC-20**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.44 | [40:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2440s) | 🟢 USEFUL | When should CloudWatch alarms notify a developer? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [41:02](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2462s) watch if the utilization is going about 90% CPU or memory utilization so those are configured for all the moments or only for production production not for the movements um I seen prepr and fraud only<br>[41:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2483s) okay and what if uh the things go was very wrong in development moment how do you manage that yeah we we check uh uh the logs and yeah manually or uh some instances are getting spin up if the | Alarms should fire for meaningful symptoms, such as sustained failures, latency, or resource exhaustion. For example, a high error-rate alarm can trigger an on-call notification. I include enough context to triage quickly and avoid alerting on every minor log entry. Alert quality matters more than alarm count. |

<a id="ia-85"></a>

## IA-85 — When is asynchronous messaging better than a direct REST call?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.46 | [43:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2590s) | 🟢 USEFUL | When is asynchronous messaging better than a direct REST call? |
| YT-8.47 | [44:27](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2667s) | 🟢 USEFUL | Follow-up: When is asynchronous messaging better than a direct REST call? |
| YT-8.48 | [45:36](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2736s) | 🟢 USEFUL | Follow-up: When is asynchronous messaging better than a direct REST call? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [43:26](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2606s) want to connect with the Q uh then configuration we have to mention for connecting with the Q there will be some producer microservices Services some consumer microservices there will be uh putting<br>[43:42](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2622s) or getting the messages from that Q or what any any specific Q implementation you have done like IBM mq I used in my project once anything about kka uh kka no I don't have much | Asynchronous messaging is useful when the caller does not need an immediate result. For example, after an order succeeds, a service can publish an event for email or analytics. The consumer processes it later. This reduces coupling but requires retry, duplicate-handling, and eventual-consistency planning. |

<a id="is-37"></a>

## IS-37 — How can Spring AOP record method entry and exit automatically?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.51 | [48:12](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2892s) | 🟢 USEFUL | How can Spring AOP record method entry and exit automatically? |
| YT-8.52 | [49:23](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2963s) | 🟢 USEFUL | Follow-up: How can Spring AOP record method entry and exit automatically? |
| YT-8.53 | [50:30](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3030s) | 🟢 USEFUL | Follow-up: How can Spring AOP record method entry and exit automatically? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [48:34](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2914s) logging at the end I have to do so of 100 methods 200 logs bad thing right so writing same thing that method started at this method ended at this you could have used aop segregated the logging<br>[48:48](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2928s) segregated the business so rather than having 100 lines of code one line two line of code and you are done yes so it will reduce your code uh duplic maintenance also become easy yes | An @Around advice can time an intercepted method and log entry, completion, or failure without adding logging code to every method. For example, I can measure all service methods through one aspect. I keep logging useful and avoid recording secrets. Spring AOP proxy rules affect which calls are intercepted. |
