# YT-3 — Mock Interview | Core Java Mock Interview Question and Answers | Code Decode

**Video:** https://www.youtube.com/watch?v=d22oNW1W6ms · **27 distinct interview questions** · **50 curated timestamp sections**.

[Pure video chronological timeline](timeline.md) · [Unedited full linked transcript](transcript.md) · [Coverage audit](coverage-audit.md)

⭐ means this interview question already exists elsewhere in the library, so its permanent ID is reused.

## Find a question

| Watch | Question |
|---|---|
| [1:21](https://www.youtube.com/watch?v=d22oNW1W6ms&t=81s) | [IA-23 — Why do microservices need service registration and discovery?](#ia-23) |
| [4:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=273s) | [IA-24 — How is client-side load balancing related to service discovery?](#ia-24) |
| [5:47](https://www.youtube.com/watch?v=d22oNW1W6ms&t=347s) | [IA-25 — Why is discovery especially valuable in cloud deployments?](#ia-25) |
| [7:14](https://www.youtube.com/watch?v=d22oNW1W6ms&t=434s) | [IA-26 — How do you avoid a single point of failure in service discovery?](#ia-26) |
| [8:21](https://www.youtube.com/watch?v=d22oNW1W6ms&t=501s) | [IA-27 — Why use an API gateway in front of microservices?](#ia-27) |
| [10:36](https://www.youtube.com/watch?v=d22oNW1W6ms&t=636s) | [IS-13 — How would you configure role-based access to Spring Boot endpoints?](#is-13) |
| [12:37](https://www.youtube.com/watch?v=d22oNW1W6ms&t=757s) | [IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?](#is-2) ⭐ |
| [14:29](https://www.youtube.com/watch?v=d22oNW1W6ms&t=869s) | [IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?](#is-3) ⭐ |
| [16:46](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1006s) | [IS-4 — What information must not be stored in JWT claims, and why?](#is-4) ⭐ |
| [17:51](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1071s) | [IA-28 — How do synchronous HTTP and asynchronous messaging differ between services?](#ia-28) |
| [18:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1113s) | [IA-29 — How would you reduce latency between microservices?](#ia-29) |
| [20:54](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1254s) | [IC-13 — How do you centralize logs from many microservices?](#ic-13) |
| [22:08](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1328s) | [IC-14 — What are Elasticsearch, Logstash, Kibana, Prometheus, and Grafana used for?](#ic-14) |
| [24:25](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1465s) | [IS-14 — What are Spring Boot Actuator health and metrics endpoints used for?](#is-14) ⭐ |
| [25:24](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1524s) | [IS-15 — How can @Cacheable reduce repeated database calls?](#is-15) ⭐ |
| [26:28](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1588s) | [IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.](#is-7) ⭐ |
| [27:42](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1662s) | [IA-30 — How do you publish REST API documentation to consumers?](#ia-30) |
| [29:25](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1765s) | [IS-16 — How would you document only selected endpoints for one API consumer?](#is-16) |
| [30:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1833s) | [IA-31 — How do you version a REST API without breaking old clients?](#ia-31) |
| [32:38](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1958s) | [IJ-146 — When should shared Java logic be extracted into a utility class?](#ij-146) |
| [33:52](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2032s) | [IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production?](#is-10) ⭐ |
| [35:13](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2113s) | [IS-17 — How can configuration changes reach running Spring services?](#is-17) |
| [37:55](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2275s) | [IC-15 — How do Jenkins and Argo CD divide CI and CD responsibilities?](#ic-15) |
| [39:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2381s) | [IC-16 — Why publish Docker images to a container registry?](#ic-16) ⭐ |
| [41:09](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2469s) | [IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.](#ic-4) ⭐ |
| [43:27](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2607s) | [IC-17 — How does Argo CD detect and apply a new application image version?](#ic-17) |
| [45:32](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2732s) | [IC-18 — How do you monitor Kubernetes services and alert the on-call team?](#ic-18) |

## Non-question source context — intros, promotions and closing

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.1 | [0:00](https://www.youtube.com/watch?v=d22oNW1W6ms&t=0s) | 🟡 INTRO | Interview introduction and candidate background |
| YT-3.3 | [2:17](https://www.youtube.com/watch?v=d22oNW1W6ms&t=137s) | 🔴 NO NEED | Sponsored course promotion, not an interview question |
| YT-3.4 | [2:30](https://www.youtube.com/watch?v=d22oNW1W6ms&t=150s) | 🔴 NO NEED | Sponsored course promotion |
| YT-3.5 | [3:46](https://www.youtube.com/watch?v=d22oNW1W6ms&t=226s) | 🔴 NO NEED | Sponsored course promotion |
| YT-3.49 | [47:49](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2869s) | 🔴 NO NEED | Interview feedback and closing |
| YT-3.50 | [49:04](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2944s) | 🔴 NO NEED | End of interview or closing remarks |

<a id="ia-23"></a>

## IA-23 — Why do microservices need service registration and discovery?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.2 | [1:21](https://www.youtube.com/watch?v=d22oNW1W6ms&t=81s) | 🟢 USEFUL | Why do microservices need service registration and discovery? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:37](https://www.youtube.com/watch?v=d22oNW1W6ms&t=97s) there are when when the application was deployed into the cloud the M main theme of the microservices is to make them ion Services resilient and scalable so when it comes to scalable in the cloud<br>[1:49](https://www.youtube.com/watch?v=d22oNW1W6ms&t=109s) environment each servic is going to have different instances Bas according to the load requirements that time every every instance has its own IP address so to get the details of the IP address and | Service discovery maps a service name to healthy running instances. For example, an order service can find inventory instances without hardcoding IP addresses that change during scaling. The key is that services discover current destinations instead of storing addresses in application code. |

<a id="ia-24"></a>

## IA-24 — How is client-side load balancing related to service discovery?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.6 | [4:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=273s) | 🟢 USEFUL | How is client-side load balancing related to service discovery? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [4:45](https://www.youtube.com/watch?v=d22oNW1W6ms&t=285s) balancing okay uh when it comes to client side load balancing the services are intercom interconnected to get the information as a single transaction it was like a<br>[4:57](https://www.youtube.com/watch?v=d22oNW1W6ms&t=297s) single transaction m so if the services are interconnected we might know we don't need to check whether the particular service instance is up or running so to avoid that and get the | A client-side load balancer obtains available service instances and picks one for a request. For example, several inventory replicas can receive orders using a round-robin policy. Discovery finds the replicas and load balancing selects one; those are related but different jobs. |

<a id="ia-25"></a>

## IA-25 — Why is discovery especially valuable in cloud deployments?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.7 | [5:47](https://www.youtube.com/watch?v=d22oNW1W6ms&t=347s) | 🟢 USEFUL | Why is discovery especially valuable in cloud deployments? |
| YT-3.8 | [7:03](https://www.youtube.com/watch?v=d22oNW1W6ms&t=423s) | 🟢 USEFUL | Follow-up: Why is discovery especially valuable in cloud deployments? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [6:11](https://www.youtube.com/watch?v=d22oNW1W6ms&t=371s) cloud based on the load and the requirements the application has to scale up and scale down according to the load base So based on load base um it can have multiple instances with the help of load<br>[6:26](https://www.youtube.com/watch?v=d22oNW1W6ms&t=386s) balancer the load will be distributed to different services so we don't need to check every service that which is having which IP address the with the yeah that's it yes I agree that's perfectly | Cloud deployments create and remove instances dynamically, so fixed service URLs go stale quickly. A registry or platform DNS keeps track of current endpoints. For example, scaling inventory from two pods to five should not require redeploying order service. The main idea is to separate service identity from instance addresses. |

<a id="ia-26"></a>

## IA-26 — How do you avoid a single point of failure in service discovery?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.9 | [7:14](https://www.youtube.com/watch?v=d22oNW1W6ms&t=434s) | 🟢 USEFUL | How do you avoid a single point of failure in service discovery? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [7:29](https://www.youtube.com/watch?v=d22oNW1W6ms&t=449s) you prevent the uh failure of your service Discovery the service the service Discovery itself contains uh several instances so each is going to communicate with each other and<br>[7:43](https://www.youtube.com/watch?v=d22oNW1W6ms&t=463s) exchanges the information sometimes the each instance is going to cat that information so it was around 15 to 10 seconds the time it don't need to get the information correct I agree that in | Run more than one registry instance, replicate needed state, and configure clients to tolerate temporary failures. For example, losing one Eureka server should not instantly stop healthy services communicating. Cached service locations can help temporarily, but health and recovery rules still matter. |

<a id="ia-27"></a>

## IA-27 — Why use an API gateway in front of microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.10 | [8:21](https://www.youtube.com/watch?v=d22oNW1W6ms&t=501s) | 🟢 USEFUL | Why use an API gateway in front of microservices? |
| YT-3.11 | [9:37](https://www.youtube.com/watch?v=d22oNW1W6ms&t=577s) | 🟢 USEFUL | Follow-up: Why use an API gateway in front of microservices? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [8:36](https://www.youtube.com/watch?v=d22oNW1W6ms&t=516s) when it comes to security um security and different patterns that will help that makes the application resilient and resilient and secure so with that to provide a single<br>[8:50](https://www.youtube.com/watch?v=d22oNW1W6ms&t=530s) entry point for all the microservices and if we had implemented the security and other patterns inside the single micro for each micros service the size of the micros service will be more and | An API gateway is a single public entry point that routes requests to the right backend service. For example, the frontend calls one gateway for orders and products rather than remembering separate service hosts. It can also centralize rate limiting and authentication checks, while backend services still enforce their own authorization. |

<a id="is-13"></a>

## IS-13 — How would you configure role-based access to Spring Boot endpoints?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.12 | [10:36](https://www.youtube.com/watch?v=d22oNW1W6ms&t=636s) | 🟢 USEFUL | How would you configure role-based access to Spring Boot endpoints? |
| YT-3.13 | [11:42](https://www.youtube.com/watch?v=d22oNW1W6ms&t=702s) | 🟢 USEFUL | Follow-up: How would you configure role-based access to Spring Boot endpoints? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [10:53](https://www.youtube.com/watch?v=d22oNW1W6ms&t=653s) is going to connect with the backend application which is only the AP Gateway for services we had provide method level security which is like role based authentication nice role based<br>[11:04](https://www.youtube.com/watch?v=d22oNW1W6ms&t=664s) authentication and US based authentication and how did you implement role based authentication uh how uh we had created a separate configuration class inside the | In Spring Security I configure a SecurityFilterChain for request rules and enable method security when needed. For example, only an ADMIN role should open an admin endpoint, while public product listings may be permitted. I verify the token and enforce the rule on the server; hiding a button in the UI is not security. |

<a id="is-2"></a>

## IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0? ⭐

⭐ **Repeated interview question:** reused **IS-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.14 | [12:37](https://www.youtube.com/watch?v=d22oNW1W6ms&t=757s) | 🟢 USEFUL | How do OAuth 2.0, OpenID Connect, and Okta fit together? |
| YT-3.15 | [13:52](https://www.youtube.com/watch?v=d22oNW1W6ms&t=832s) | 🟢 USEFUL | Follow-up: How do OAuth 2.0, OpenID Connect, and Okta fit together? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [12:50](https://www.youtube.com/watch?v=d22oNW1W6ms&t=770s) so what format of token you have used for communication what type of token is it is it a basic like see basic 64 encoded token or a proper JWT token yeah the proper JWT token we had<br>[13:06](https://www.youtube.com/watch?v=d22oNW1W6ms&t=786s) used okay and U you have so how these U communication goes so you have told me about the authorization part that you have Ro based access controls over your apis but how is authentication done for | OAuth 2.0 provides delegated authorization, while OpenID Connect adds an identity layer for sign-in. Okta can act as the provider issuing tokens. For example, a frontend signs users in through Okta and sends an access token to a Spring API. The API validates the token and checks scopes or roles. |

<a id="is-3"></a>

## IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering? ⭐

⭐ **Repeated interview question:** reused **IS-3**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.16 | [14:29](https://www.youtube.com/watch?v=d22oNW1W6ms&t=869s) | 🟢 USEFUL | How does a Spring resource server validate a JWT? |
| YT-3.17 | [15:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=941s) | 🟢 USEFUL | Follow-up: How does a Spring resource server validate a JWT? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=881s) particular communication between the front end and your back end what secures your uh communication how is your communication secured with JWT token what that JWT token has that<br>[14:53](https://www.youtube.com/watch?v=d22oNW1W6ms&t=893s) your communication from front end to back end is secured okay when it comes to JWT token it contains a header payload and the signature part but signature part is optional but when it comes to payload | A resource server validates a JWT signature using a trusted key, then checks expiry, issuer, audience, and permissions as appropriate. For example, a forged admin role should fail signature verification. Base64 decoding alone does not validate a token or protect the connection; HTTPS is also required. |

<a id="is-4"></a>

## IS-4 — What information must not be stored in JWT claims, and why? ⭐

⭐ **Repeated interview question:** reused **IS-4**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.18 | [16:46](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1006s) | 🟢 USEFUL | Which JWT claims are safe to expose to clients? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [17:00](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1020s) you you said there is something called as body uh in the JG token that is the second part in the three parts of it so what does body contains in JWT token body contains<br>[17:16](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1036s) the the data which is like a request body which contains information related to the particular user like response body not the response body yes that's right that it contains data about the | A typical signed JWT payload is encoded, not encrypted, so clients can read its claims. For example, a token may carry a subject and roles, but it should not include a password or secret. The signature helps detect tampering; confidential data belongs in protected storage. |

<a id="ia-28"></a>

## IA-28 — How do synchronous HTTP and asynchronous messaging differ between services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.19 | [17:51](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1071s) | 🟢 USEFUL | How do synchronous HTTP and asynchronous messaging differ between services? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [18:05](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1085s) and asynchronous communication okay for synchronous communication we are using open fine Cent for communication between the microservices for asynchronous we are using<br>[18:17](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1097s) Kafka okay as a message broker for as agree U now I can say that there is some uh latency getting into induced while my Comm micros Services communicate so what happens is one | Synchronous HTTP asks another service for a response now; asynchronous messaging sends an event for processing later. For example, checkout might synchronously reserve stock but publish an email notification event. I choose based on whether the caller truly needs the result before continuing. |

<a id="ia-29"></a>

## IA-29 — How would you reduce latency between microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.20 | [18:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1113s) | 🟢 USEFUL | How would you reduce latency between microservices? |
| YT-3.21 | [19:43](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1183s) | 🟢 USEFUL | Follow-up: How would you reduce latency between microservices? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [19:01](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1141s) data is going to related to the enti database related queries so we can um write the efficient queries with that uh we can reduce that and if there are particular get apas that data is not<br>[19:15](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1155s) going to change much much time we can use uh cachy for to store the data okay I agree also for for for the query optimization we can use indexes on our data basis if we have the proper SQL | First I measure which call or query is slow. Then I can optimize queries, add a useful cache, reduce unnecessary network hops, or send nonurgent work to a queue. For example, order confirmation email should not delay the checkout response. Measure first so the optimization fixes the actual bottleneck. |

<a id="ic-13"></a>

## IC-13 — How do you centralize logs from many microservices?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.22 | [20:54](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1254s) | 🟢 USEFUL | How do you centralize logs from many microservices? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [21:10](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1270s) inside this uh War error debug okay and info with this level so we are going to print the state login statements okay U so you print the logs now how do you see those logs which are getting<br>[21:30](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1290s) generated okay in our local environment there is there was only a single instance so we can uh see those logs inside the console so but when it comes to microservice | Each service writes structured logs with a request or trace identifier, and an agent forwards them to centralized storage. For example, I can follow an order request across three services by one trace ID. This is much more useful than opening separate pod consoles during an incident. |

<a id="ic-14"></a>

## IC-14 — What are Elasticsearch, Logstash, Kibana, Prometheus, and Grafana used for?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.23 | [22:08](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1328s) | 🟢 USEFUL | What are Elasticsearch, Logstash, Kibana, Prometheus, and Grafana used for? |
| YT-3.24 | [23:24](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1404s) | 🟢 USEFUL | Follow-up: What are Elasticsearch, Logstash, Kibana, Prometheus, and Grafana used for? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [22:24](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1344s) elk stack and how is it useful for centralized logging okay when it comes uh first of all the every micros service has to integ has to integrate has a must had a dependency<br>[22:40](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1360s) which is related to log stest log stest which collects and stores all the logs related to the particular micro particular service when it comes to elastic elastic log St is collect and filters | Logstash collects and processes log events, Elasticsearch indexes them, and Kibana explores them. Prometheus collects time-series metrics, and Grafana builds dashboards. For example, a slow checkout can be investigated using log events and latency charts. Logs explain events; metrics show trends. |

<a id="is-14"></a>

## IS-14 — What are Spring Boot Actuator health and metrics endpoints used for? ⭐

⭐ **Repeated interview question:** reused **IS-14**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.25 | [24:25](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1465s) | 🟢 USEFUL | What are Spring Boot Actuator health and metrics endpoints used for? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [24:40](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1480s) application which includes health check Readiness check health check includes combination of Readiness and livess and provides information related to Heap space memory that information we get from the<br>[24:54](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1494s) accor and it was very helpful in the micros service en so the micros service the when it comes to Gateway the Gateway has to start only once all the services are up | Spring Boot Actuator exposes operational endpoints such as health, info, and metrics when configured. For example, Kubernetes can use readiness and liveness endpoints to decide whether a pod should receive traffic or restart. Management endpoints need careful exposure and security because they reveal application internals. |

<a id="is-15"></a>

## IS-15 — How can @Cacheable reduce repeated database calls? ⭐

⭐ **Repeated interview question:** reused **IS-15**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.26 | [25:24](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1524s) | 🟢 USEFUL | How can @Cacheable reduce repeated database calls? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [25:36](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1536s) performance so there are some particular get methods which retries the information okay for get methods we can use we had used at theate cachable annotation for that methods so we can provide the cach<br>[25:52](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1552s) information for a particular time period we can Define that inside the application file application. properties file so it will it will not make database calls for every of the time so reducing | Spring's @Cacheable can store a method result under a cache key, so repeated calls with the same input avoid unnecessary work. For example, a rarely changed product category list can come from a cache. I still plan eviction or expiry because cached data may become stale. |

<a id="is-7"></a>

## IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope. ⭐

⭐ **Repeated interview question:** reused **IS-7**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.27 | [26:28](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1588s) | 🟢 USEFUL | How does Hibernate caching differ from Spring method caching? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:43](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1603s) then with the help of entity is the cash and other things is going to use internally this right or manager so uh yes uh you can use at theate cashable and atate cash and all<br>[27:02](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1622s) these things these if if you're using it on your entity and entity managers in session then it is the internal one that is provided by hnet for you and there are two levels of caching uh for the | Hibernate's first-level cache is scoped to a persistence context; second-level caching is optional and shared across sessions within a session factory. Spring method caching instead caches method results through a configured cache manager. For example, reloading one managed entity is different from caching the output of a service method. |

<a id="ia-30"></a>

## IA-30 — How do you publish REST API documentation to consumers?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.28 | [27:42](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1662s) | 🟢 USEFUL | How do you publish REST API documentation to consumers? |
| YT-3.29 | [28:58](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1738s) | 🟢 USEFUL | Follow-up: How do you publish REST API documentation to consumers? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [27:56](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1676s) contract like to your cons consumer that you can use this rest endpoint using these parameters these request parameters these query parameters this response body this is how you going to<br>[28:06](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1686s) get response back if you do not provide this query parameter I'm going to respond you with 400 bad request that you have not given this to me so all this contract is so much to tell mouth | I describe endpoint paths, request parameters, response shapes, and error codes using an API contract such as OpenAPI. For example, a client can see exactly how to call GET orders by ID. A shared contract keeps frontend and backend teams aligned and exposes changes before deployment. |

<a id="is-16"></a>

## IS-16 — How would you document only selected endpoints for one API consumer?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.30 | [29:25](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1765s) | 🟢 USEFUL | How would you document only selected endpoints for one API consumer? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [29:57](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1797s) having access to and the particular APS we can provide type of security inser the annotations right with help of is it possible you can give role based exess also as far as<br>[30:16](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1816s) I yes some kind of uh exess you can give or else you can have two different type of documentations also both the ways you can uh have this achieved uh next I'll uh go ahead U again a | I would publish a filtered OpenAPI definition or use separate documentation groups for different audiences. For example, a partner should see the partner endpoints but not internal operational APIs. Documentation filtering improves clarity; actual endpoint access must still be enforced with authentication and authorization. |

<a id="ia-31"></a>

## IA-31 — How do you version a REST API without breaking old clients?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.31 | [30:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1833s) | 🟢 USEFUL | How do you version a REST API without breaking old clients? |
| YT-3.32 | [31:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1901s) | 🟢 USEFUL | Follow-up: How do you version a REST API without breaking old clients? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [30:57](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1857s) compl completely so how do you manage these uh changing uh require changed version so Suppose there are two consumers A and B now a doesn't want a new response he says that my everything<br>[31:11](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1871s) will break I don't want that so how do you manage that one particular Endo behaves in two different ways for two different consumers okay we can the we can use the versioning which is inside the the | I can expose a new version through a path, header, or media type while supporting the old contract during migration. For example, /v1/orders can continue working as /v2/orders introduces a changed response. Versioning is a compatibility strategy; it does not replace regression tests. |

<a id="ij-146"></a>

## IJ-146 — When should shared Java logic be extracted into a utility class?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.33 | [32:38](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1958s) | 🟢 USEFUL | When should shared Java logic be extracted into a utility class? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [32:53](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1973s) controllers or the components you can use the same code by injecting an autog it or making it static one and just use utilizing that using the uh static uh class dot method name if you<br>[33:07](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1987s) don't have any property access into it okay uh coming to the properties how did you manage uh your profilings in Spring boot application all of our profiles and application related to properties fails | If several callers need the same stateless calculation or formatting rule, a small utility can remove duplication. For example, one formatter can normalize order references for two API versions. I avoid putting all business logic into one giant static utility class because it becomes hard to test and maintain. |

<a id="is-10"></a>

## IS-10 — How do Spring Boot profiles manage configuration across development, QA, staging and production? ⭐

⭐ **Repeated interview question:** reused **IS-10**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.34 | [33:52](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2032s) | 🟢 USEFUL | How do Spring profiles and a config server work together? |
| YT-3.35 | [34:59](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2099s) | 🟢 USEFUL | Follow-up: How do Spring profiles and a config server work together? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:06](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2046s) must be some uh remote repository where you are keeping these properties common right yes so what do you use for the version controls for this particular application that you have as a config<br>[34:20](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2060s) server yeah we are storing all those properties related files inside the uh GitHub repository that's Version Control System for you okay so how how so basically there must be a hook created | Profiles select environment-specific settings, while a config server can provide those settings from a central source. For example, development and production may use different database addresses without changing Java code. Secrets still need proper protection and access control. |

<a id="is-17"></a>

## IS-17 — How can configuration changes reach running Spring services?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.36 | [35:13](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2113s) | 🟢 USEFUL | How can configuration changes reach running Spring services? |
| YT-3.37 | [36:24](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2184s) | 🟢 USEFUL | Follow-up: How can configuration changes reach running Spring services? |
| YT-3.38 | [37:30](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2250s) | 🟢 USEFUL | Follow-up: How can configuration changes reach running Spring services? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:25](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2125s) to use on a class to have that Dynamic uh property injected into the class anything something called as refresh scope to pull uh the refreshed Dynamic Property is that needed no okay in the code<br>[35:48](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2148s) might config server and config client dependen based on these dependencies the particular microservices okay config server is acting as as a server and config client | Changing a Git file does not automatically change every running bean. A Spring Cloud configuration setup may use refresh events, Spring Cloud Bus, or a redeployment, depending on how properties are consumed. For example, an updated timeout might need an explicit refresh step. I always verify which settings are dynamically refreshable. |

<a id="ic-15"></a>

## IC-15 — How do Jenkins and Argo CD divide CI and CD responsibilities?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.39 | [37:55](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2275s) | 🟢 USEFUL | How do Jenkins and Argo CD divide CI and CD responsibilities? |
| YT-3.40 | [39:01](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2341s) | 🟢 USEFUL | Follow-up: How do Jenkins and Argo CD divide CI and CD responsibilities? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [38:17](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2297s) are using genkins when it comes to CD we are using Argo CD which will handle all the deployments related to the kubernetes okay so you have used kubernetes for your deployment so what<br>[38:29](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2309s) CL Cloud platform you have used for your deployment we are using uh AWS services and what all services you have used for your AWS club for your appli we had used we had used several services like uh | Jenkins can build and test an application, then publish a versioned image. Argo CD watches desired Kubernetes configuration in Git and reconciles the cluster to match it. For example, a release updates the image tag in Git; Argo CD deploys it. This separates artifact creation from deployment reconciliation. |

<a id="ic-16"></a>

## IC-16 — Why publish Docker images to a container registry? ⭐

⭐ **Repeated interview question:** reused **IC-16**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.41 | [39:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2381s) | 🟢 USEFUL | Why publish Docker images to a container registry? |
| YT-3.42 | [40:58](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2458s) | 🟢 USEFUL | Follow-up: Why publish Docker images to a container registry? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [39:55](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2395s) nice that is because uh it gives you much more secure image uh retention when you use your cloud-based registry storage rather than the common public one like dockerhub nice that's perfect<br>[40:06](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2406s) approach uh that the company has used nice uh for EK for the kubernetes management that is uh for you have used eks yes okay Aro CD for managing the kubernetes Argo CD is for continuous | A registry stores versioned images that deployment tools can pull. For example, after Jenkins builds order-service:1.2, Kubernetes can run the exact tested image from a registry. Using fixed tags or digests improves repeatability; a Docker image is different from a running container. |

<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates. ⭐

⭐ **Repeated interview question:** reused **IC-4**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.43 | [41:09](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2469s) | 🟢 USEFUL | What steps belong in a typical GitHub-to-Kubernetes CI/CD pipeline? |
| YT-3.44 | [42:26](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2546s) | 🟢 USEFUL | Follow-up: What steps belong in a typical GitHub-to-Kubernetes CI/CD pipeline? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [41:23](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2483s) the jenin C pipeline it is going to get the latest repo from the GitHub repository and it generates an artifact based on that artifact it is going to get get the unit tests done and Son<br>[41:38](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2498s) our code quality and code coverage it is going to test once it meets the particular particular Point particular points that we had different yeah threshold once it done it is going | A typical flow is commit, build, unit tests, quality and security checks, image creation, registry push, and deployment verification. For example, a failed test should stop the pipeline before the image reaches production. The point is to make each promotion visible and repeatable. |

<a id="ic-17"></a>

## IC-17 — How does Argo CD detect and apply a new application image version?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.45 | [43:27](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2607s) | 🟢 USEFUL | How does Argo CD detect and apply a new application image version? |
| YT-3.46 | [44:33](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2673s) | 🟢 USEFUL | Follow-up: How does Argo CD detect and apply a new application image version? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [43:45](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2625s) the one that is deployed is an old image right yes a new image is arrived so a new container has to be started spinned up to starting a new uh container you need a kubernetes who is a a container<br>[44:02](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2642s) orchestrator for you so now Aro CD comes into picture who fetches this latest image and uh does the deployment for you that's fine and the do the image is generated at the end of | Argo CD compares the cluster with desired manifests stored in Git. A pipeline or image updater commits an approved new image tag, and Argo CD reconciles the deployment. For example, changing the order-service tag in Git triggers rollout when synchronization is enabled. Pushing an image alone does not guarantee the manifest changes. |

<a id="ic-18"></a>

## IC-18 — How do you monitor Kubernetes services and alert the on-call team?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.47 | [45:32](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2732s) | 🟢 USEFUL | How do you monitor Kubernetes services and alert the on-call team? |
| YT-3.48 | [46:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2801s) | 🟢 USEFUL | Follow-up: How do you monitor Kubernetes services and alert the on-call team? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [45:44](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2744s) they're not facing the downtime okay during the application is running in the production environment is service having it own those Matrix okay okay Matrix yeah related to The Matrix the Prometheus<br>[46:04](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2764s) will get all the matric from the particular service and it is going to V visualize inside the grafana dashboard so grafana provides different custom dashb uh which in that we can | I collect application and infrastructure metrics, define thresholds or symptom-based alerts, and route actionable incidents to the right person. For example, sustained 5xx errors are more useful than an occasional harmless log message. Good alerts include service name, severity, and a dashboard link. |
