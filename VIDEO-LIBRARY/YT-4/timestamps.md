# YT-4 — Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode |

**Video:** https://www.youtube.com/watch?v=ekLB9t9DBAk · **42 distinct interview questions** · **82 curated timestamp sections**.

[Pure video chronological timeline](timeline.md) · [Unedited full linked transcript](transcript.md) · [Coverage audit](coverage-audit.md)

⭐ means this interview question already exists elsewhere in the library, so its permanent ID is reused.

## Find a question

| Watch | Question |
|---|---|
| [0:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=38s) | [IJ-147 — Which Java 8 features are most important for everyday backend code?](#ij-147) ⭐ |
| [1:31](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=91s) | [IJ-148 — What is a functional interface and why is it useful?](#ij-148) |
| [2:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=131s) | [IJ-149 — Why is Java not considered a purely object-oriented language?](#ij-149) ⭐ |
| [3:24](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=204s) | [IJ-150 — How does HashMap treeification improve collision performance in Java 8?](#ij-150) |
| [4:36](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=276s) | [IJ-151 — What changed from PermGen to Metaspace in Java 8?](#ij-151) |
| [5:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=318s) | [IJ-152 — Why were default methods added to Java interfaces?](#ij-152) |
| [6:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=405s) | [IJ-153 — Why does Java disallow extending two classes but allow multiple interfaces?](#ij-153) |
| [8:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=512s) | [IJ-154 — How do you resolve conflicting default methods from two Java interfaces?](#ij-154) ⭐ |
| [12:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=734s) | [IJ-155 — What are Optional.empty, of, and ofNullable used for?](#ij-155) |
| [14:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=861s) | [IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.](#ia-5) ⭐ |
| [16:29](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=989s) | [IA-32 — How do Saga orchestration and choreography compare?](#ia-32) |
| [20:48](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1248s) | [IS-18 — What does @Transactional do inside one Spring service?](#is-18) |
| [21:56](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1316s) | [IA-33 — How do an API gateway, service discovery, and load balancing differ?](#ia-33) |
| [23:44](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1424s) | [IC-19 — How do trace IDs and span IDs help debug distributed calls?](#ic-19) ⭐ |
| [25:34](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1534s) | [IC-20 — How would you send production alerts using AWS CloudWatch?](#ic-20) ⭐ |
| [26:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1578s) | [IC-21 — How do application log statements reach Elasticsearch and Kibana?](#ic-21) |
| [27:08](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1628s) | [IS-19 — How does Spring Cloud Config share configuration among microservices?](#is-19) ⭐ |
| [29:15](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1755s) | [IC-2 — How do feature branches progress through QA, staging and production?](#ic-2) ⭐ |
| [31:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1913s) | [IC-6 — How would you run and scale ten microservices with Kubernetes?](#ic-6) ⭐ |
| [33:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2012s) | [IC-22 — How do Kubernetes Services handle changing pod IP addresses?](#ic-22) |
| [34:56](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2096s) | [IS-20 — What changed when moving to Spring Boot 3?](#is-20) |
| [36:20](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2180s) | [IS-21 — How can you replace embedded Tomcat in a Spring Boot application?](#is-21) |
| [38:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2321s) | [IJ-156 — How do you implement a lazy Singleton safely in multithreaded Java?](#ij-156) ⭐ |
| [43:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2591s) | [IS-22 — What are singleton, prototype, request, and session bean scopes?](#is-22) ⭐ |
| [45:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2718s) | [IS-23 — Can changing a singleton Spring bean affect different consumers?](#is-23) |
| [47:40](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2860s) | [IJ-157 — How is a classic Java Singleton different from a Spring singleton bean?](#ij-157) |
| [50:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3033s) | [IT-6 — How do behavior-driven tests differ from test-driven development?](#it-6) |
| [51:47](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3107s) | [IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?](#it-2) ⭐ |
| [54:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3266s) | [IT-7 — What do JUnit 5 @BeforeEach and @BeforeAll do?](#it-7) |
| [56:08](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3368s) | [IA-34 — What does the SOLID single-responsibility principle mean?](#ia-34) ⭐ |
| [58:17](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3497s) | [IA-35 — How does the open-closed principle apply to payment integrations?](#ia-35) ⭐ |
| [59:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3566s) | [IS-24 — How do JPA derived queries and @Query compare?](#is-24) ⭐ |
| [1:02:55](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3775s) | [IJ-158 — Why must JPA repository ID types use wrapper types?](#ij-158) |
| [1:03:43](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3823s) | [ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?](#id-1) ⭐ |
| [1:05:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3900s) | [IJ-159 — When are parallel threads a poor substitute for query optimization?](#ij-159) |
| [1:05:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3957s) | [ID-2 — Explain table partitioning versus database sharding.](#id-2) ⭐ |
| [1:07:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4041s) | [IS-25 — How do you model a many-to-many JPA relationship?](#is-25) |
| [1:08:27](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4107s) | [IA-36 — What are Kafka topics, partitions, and consumer groups?](#ia-36) |
| [1:10:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4245s) | [IS-4 — What information must not be stored in JWT claims, and why?](#is-4) ⭐ |
| [1:13:29](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4409s) | [IS-26 — How would you configure CORS for a Spring Boot API?](#is-26) ⭐ |
| [1:17:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4652s) | [IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.](#ic-4) ⭐ |
| [1:19:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4754s) | [IA-20 — How would you diagnose Kafka consumer lag in a distributed system?](#ia-20) ⭐ |

## Non-question source context — intros, promotions and closing

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.1 | [0:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=0s) | 🟡 INTRO | Interview introduction and candidate background |
| YT-4.81 | [1:20:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4826s) | 🔴 NO NEED | Interview closing |
| YT-4.82 | [1:21:02](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4862s) | 🔴 NO NEED | End of interview or closing remarks |

<a id="ij-147"></a>

## IJ-147 — Which Java 8 features are most important for everyday backend code? ⭐

⭐ **Repeated interview question:** reused **IJ-147**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.2 | [0:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=38s) | 🟢 USEFUL | Which Java 8 features are most important for everyday backend code? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [0:51](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=51s) introduced in Java uh related to functional interfaces and mostly Java they have introduced uh for functional program programming before Java uh there was no concept of functional programming<br>[1:03](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=63s) in Java and also Lambda Expressions uh default and static methods in interfaces predefined interfaces uh like predicate function consumer and Method reference and | Java 8 introduced lambdas, method references, streams, Optional, and the modern date-time API. For example, a stream can filter a list of active customers without writing an explicit loop. The key is to choose features that clarify the code instead of using them everywhere. |

<a id="ij-148"></a>

## IJ-148 — What is a functional interface and why is it useful?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.3 | [1:31](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=91s) | 🟢 USEFUL | What is a functional interface and why is it useful? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:44](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=104s) programming yeah functional programming was introduced such that we can pass a function as an argument to a method and also functional interface was introduced uh such that we can have only one<br>[1:58](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=118s) abstract method in the interface we can make uh an interface as functional interface by forcing it as by forcing like we can use at functional interface annotation about the interface | A functional interface has one abstract method, which means a lambda can provide its behavior. For example, Predicate&lt;String&gt; can test whether a name is blank. Default and static methods do not increase the abstract-method count. I use functional interfaces when behavior needs to be passed as a value. |

<a id="ij-149"></a>

## IJ-149 — Why is Java not considered a purely object-oriented language? ⭐

⭐ **Repeated interview question:** reused **IJ-149**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.4 | [2:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=131s) | 🟢 USEFUL | Why is Java not considered a purely object-oriented language? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [2:25](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=145s) primitive uh data types like in short bite so use using those uh data types we can't say that Java is a complete object oriented language okay and how do you come across<br>[2:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=158s) uh like what uh classes are around those particular Primitives which make them objectoriented we can use a concept of rer classes so which can convert the Primitive types into object oriented for | Java has primitives such as int and boolean that are not objects. Wrapper classes such as Integer let primitive values work with generic collections. For example, a List&lt;Integer&gt; can store numeric elements, but List&lt;int&gt; cannot in Java 21. So Java is strongly object-oriented without making every value an object. |

<a id="ij-150"></a>

## IJ-150 — How does HashMap treeification improve collision performance in Java 8?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.5 | [3:24](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=204s) | 🟢 USEFUL | How does HashMap treeification improve collision performance in Java 8? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [3:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=218s) into the map okay uh for example after some uh threshold value the link list will be converted into tree nice and why was that done uh in order to get the value from<br>[3:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=233s) the map uh we know that the complexity uh time complexity uh to get the value from the map will be big of one but when we are iterating through the entire link list it could be big of one so when we | When enough entries collide in one HashMap bucket and the table is sufficiently large, Java can change a linked list of nodes into a tree. For example, many keys with colliding hashes can make lookup slower; tree bins improve worst-case searching when keys can be ordered appropriately. Normal well-distributed keys usually remain fast. |

<a id="ij-151"></a>

## IJ-151 — What changed from PermGen to Metaspace in Java 8?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.6 | [4:36](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=276s) | 🟢 USEFUL | What changed from PermGen to Metaspace in Java 8? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [4:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=290s) of uh garbage collection uh they have come up instead of uh there is one particular concept of perm gen so uh I think they have come up with the new concept of perm gen in<br>[5:05](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=305s) Java so initially it was using something called as metaspace metaspace yeah from metaspace they have come up with the new concept of firm gen and any clue what changes | Java 8 removed the old permanent generation and introduced Metaspace for class metadata. Unlike PermGen, Metaspace generally uses native memory. For example, loading many dynamically generated classes can consume Metaspace. The important correction is the direction: PermGen was replaced by Metaspace, not the other way around. |

<a id="ij-152"></a>

## IJ-152 — Why were default methods added to Java interfaces?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.7 | [5:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=318s) | 🟢 USEFUL | Why were default methods added to Java interfaces? |
| YT-4.8 | [6:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=393s) | 🟢 USEFUL | Follow-up: Why were default methods added to Java interfaces? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [5:31](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=331s) default method if I talk about uh mainly it came into picture for solving the limitations of interfaces for adding more functionality to the methods in interface without breaking the<br>[5:43](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=343s) implementation of classes for example I have a class called book and also I mean I have an uh book interface and this book interface is being implemented by two other classes called fictional books | Default methods allow interfaces to add optional behavior without forcing every existing implementing class to implement a new abstract method. For example, a library can add a convenience method while preserving older implementations. Implementing classes can override it. This helped interface evolution when Java 8 introduced new library features. |

<a id="ij-153"></a>

## IJ-153 — Why does Java disallow extending two classes but allow multiple interfaces?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.9 | [6:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=405s) | 🟢 USEFUL | Why does Java disallow extending two classes but allow multiple interfaces? |
| YT-4.10 | [8:02](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=482s) | 🟢 USEFUL | Follow-up: Why does Java disallow extending two classes but allow multiple interfaces? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [6:59](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=419s) multiple inheritance is not allowed in Java okay and any way Java try to implement multiple inheritance using classes you cannot uh use multiple inheritance but using<br>[7:15](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=435s) interfaces uh you can uh use the concept or implement the concept of inheritance multiple inheritance so how you can't extend two or more please you can't extend one or more | Java classes can extend only one direct superclass, which avoids ambiguity over inherited state and implementations. A class can implement several interfaces. For example, a printer can implement both Printable and Scannable. When two interfaces provide conflicting defaults, the implementing class must resolve the conflict explicitly. |

<a id="ij-154"></a>

## IJ-154 — How do you resolve conflicting default methods from two Java interfaces? ⭐

⭐ **Repeated interview question:** reused **IJ-154**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.11 | [8:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=512s) | 🟢 USEFUL | How do you resolve conflicting default methods from two Java interfaces? |
| YT-4.12 | [9:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=590s) | 🟢 USEFUL | Follow-up: How do you resolve conflicting default methods from two Java interfaces? |
| YT-4.13 | [11:12](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=672s) | 🟢 USEFUL | Follow-up: How do you resolve conflicting default methods from two Java interfaces? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [8:54](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=534s) I have an animal class who has a method eat I have an uh fish class who whose method is eat and it just drinks water two implementations different implementations now if I extend both<br>[9:09](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=549s) animal and fish you are confused I want to eat or I want to just drink water so this is the diamond problem that is the reason classes do not have it but initially with before java8 there was no | If two unrelated interfaces provide the same default method signature, the implementing class must override that method. It can choose one implementation using InterfaceName.super.method() or provide completely new logic. For example, a class implementing two greeting interfaces can decide which greeting to use. Java requires the ambiguity to be resolved. |

<a id="ij-155"></a>

## IJ-155 — What are Optional.empty, of, and ofNullable used for?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.14 | [12:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=734s) | 🟢 USEFUL | What are Optional.empty, of, and ofNullable used for? |
| YT-4.15 | [13:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=806s) | 🟢 USEFUL | Follow-up: What are Optional.empty, of, and ofNullable used for? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [12:30](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=750s) avoid null pointer exceptions um there are different types of methods which was introduced in optional for example optional. empty optional do off and optional do off<br>[12:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=761s) nullable mainly optional. empty this method returns an empty uh optional object and indicating that uh it doesn't contain any value and also it is mainly often used to initialize any optional | Optional represents a value that may or may not exist. empty creates no value, of requires a non-null value, and ofNullable accepts null and produces an empty Optional. For example, finding a customer by ID may return Optional&lt;Customer&gt;. I check isPresent or use map and orElse instead of blindly calling get. |

<a id="ia-5"></a>

## IA-5 — Compare Saga and two-phase commit for distributed microservice transactions. ⭐

⭐ **Repeated interview question:** reused **IA-5**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.16 | [14:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=861s) | 🟢 USEFUL | How can Saga handle a distributed order transaction? |
| YT-4.17 | [15:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=938s) | 🟢 USEFUL | Follow-up: How can Saga handle a distributed order transaction? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=885s) assigned and Order reaches to you what if the payment fails in between you have to roll back all you have to cancel the order right we need to roll back yeah so the this transaction you can see is not<br>[14:59](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=899s) in one particular application it is across the whole micros services so what what kind of distributed transactions you can handle how how can you handle this particular distributed transactions | A Saga coordinates a sequence of local transactions, with compensating actions when a step fails. For example, if payment fails after reserving inventory, a compensation can release the reservation. This is not the same as a single atomic database rollback. The advantage is managing cross-service work without one global transaction. |

<a id="ia-32"></a>

## IA-32 — How do Saga orchestration and choreography compare?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.18 | [16:29](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=989s) | 🟢 USEFUL | How do Saga orchestration and choreography compare? |
| YT-4.19 | [17:36](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1056s) | 🟢 USEFUL | Follow-up: How do Saga orchestration and choreography compare? |
| YT-4.20 | [18:52](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1132s) | 🟢 USEFUL | Follow-up: How do Saga orchestration and choreography compare? |
| YT-4.21 | [19:58](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1198s) | 🟢 USEFUL | Follow-up: How do Saga orchestration and choreography compare? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:43](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1003s) is the choreography design pattern one is the orchestration design pattern so in case of uh yeah I was asking how I would like to go with yeah I'd like to go with the<br>[17:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1020s) orchestration design pattern uh because we have a centralized controller uh such that the Saga participants like Saga participants in in this case is like all the microservices uh what the local | Orchestration uses a coordinator to tell each service what step to perform; choreography lets services react to one another's events. For example, an order workflow with many branching failures may be easier to understand with an orchestrator. A small event chain may work with choreography. Both need idempotency, retries, and observable failure handling. |

<a id="is-18"></a>

## IS-18 — What does @Transactional do inside one Spring service?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.22 | [20:48](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1248s) | 🟢 USEFUL | What does @Transactional do inside one Spring service? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [21:01](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1261s) micros service okay uh for example if you are having two tables inside one particular micros service and uh after one transaction you are adding uh into the second table you got some exception<br>[21:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1274s) and you want to roll back the transaction which is happened in the first table as well over the method level you can have uh annotation called a transactional based on this annotation | Spring's @Transactional places compatible database operations inside a transaction boundary. For example, creating an invoice and its line items in one database transaction should commit together or roll back on failure. Default rollback rules typically cover unchecked exceptions. It does not automatically roll back work in a different microservice. |

<a id="ia-33"></a>

## IA-33 — How do an API gateway, service discovery, and load balancing differ?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.23 | [21:56](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1316s) | 🟢 USEFUL | How do an API gateway, service discovery, and load balancing differ? |
| YT-4.24 | [23:01](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1381s) | 🟢 USEFUL | Follow-up: How do an API gateway, service discovery, and load balancing differ? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [22:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1331s) continuously so you will give this heck to front end guy or you will try to resolve it as a backend person on your own at the back end it shouldn't be given to front end guy this should be<br>[22:22](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1342s) handled only in the back end so one one thing is related to once we get the reest directly we will not hit to the particular microservice it will be routed to a load balancer and the load | An API gateway routes incoming requests to logical services; service discovery finds their current instances; load balancing selects an instance. For example, a mobile app contacts one gateway, which locates and routes an inventory request. Each piece solves a different problem, even when a platform combines them. |

<a id="ic-19"></a>

## IC-19 — How do trace IDs and span IDs help debug distributed calls? ⭐

⭐ **Repeated interview question:** reused **IC-19**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.25 | [23:44](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1424s) | 🟢 USEFUL | How do trace IDs and span IDs help debug distributed calls? |
| YT-4.26 | [24:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1493s) | 🟢 USEFUL | Follow-up: How do trace IDs and span IDs help debug distributed calls? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [24:03](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1443s) microservices we have used Zipkin and sluth in order to have uh logging centralized logging mechanism okay okay that is okay ID yes based on the trace ID and uh and we have added different types of<br>[24:24](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1464s) dependencies for that based on that Trace ID we can understand to which Microsoft the flow is going so there's two things stce ID and span ID what is the difference between those what's the | A trace ID connects operations belonging to one request, while each span ID identifies an individual unit of work within that trace. For example, one checkout trace can contain separate HTTP and database spans. The trace ID normally remains common across services; span IDs change. This makes a request journey observable. |

<a id="ic-20"></a>

## IC-20 — How would you send production alerts using AWS CloudWatch? ⭐

⭐ **Repeated interview question:** reused **IC-20**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.27 | [25:34](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1534s) | 🟢 USEFUL | How would you send production alerts using AWS CloudWatch? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [25:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1550s) alarms so inside that particular alarm we have configured some properties So based on that properties if any AP is failing we'll get a notification to to a particular admin uh email so based on<br>[26:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1564s) that uh will react accordingly perfect perfect uh okay and how do you log in your uh source code how do you make sure that your logs that you're logging in your source code reaches | I publish meaningful metrics or collect service metrics, configure CloudWatch alarms, and route notifications through an appropriate channel such as SNS. For example, sustained high error rate can page on call. Alerts should identify the affected service and be tested, rather than simply creating one alarm per log line. |

<a id="ic-21"></a>

## IC-21 — How do application log statements reach Elasticsearch and Kibana?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.28 | [26:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1578s) | 🟢 USEFUL | How do application log statements reach Elasticsearch and Kibana? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:37](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1597s) based on this particular uh log logging statements uh it will reach to the I how is kibana integrated to your particular application how do you make sure that yes you are written writing in<br>[26:52](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1612s) your source code reaches all the logs will be moved to elastic search and from elastic search uh there is a concept of fluent D from fluentd it will be more to kibana this is the flow | Applications write log events using a logging implementation; agents such as Fluent Bit or Logstash forward them into Elasticsearch. Kibana then searches and visualizes the indexed logs. For example, filtering all ERROR entries for an order ID helps troubleshoot an incident. The pipeline is separate from the code that emits the logs. |

<a id="is-19"></a>

## IS-19 — How does Spring Cloud Config share configuration among microservices? ⭐

⭐ **Repeated interview question:** reused **IS-19**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.29 | [27:08](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1628s) | 🟢 USEFUL | How does Spring Cloud Config share configuration among microservices? |
| YT-4.30 | [28:17](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1697s) | 🟢 USEFUL | Follow-up: How does Spring Cloud Config share configuration among microservices? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [27:22](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1642s) the 10 microservices or do you keep it safely at some place and refer it from there basically we store it in a git REO or a local repo uh which is called Spring Cloud config server so we need to add<br>[27:37](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1657s) one dependency called Spring Cloud config server and also one annotation called at enable config server uh inside the application. properties we maintain all this and uh like we need to write | A Config Server serves externalized properties to participating Spring applications, often backed by a Git repository. For example, ten services can load their shared timeout settings from one managed source. Different profiles can still have overrides. Updating the source does not necessarily update running beans until refresh or restart occurs. |

<a id="ic-2"></a>

## IC-2 — How do feature branches progress through QA, staging and production? ⭐

⭐ **Repeated interview question:** reused **IC-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.31 | [29:15](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1755s) | 🟢 USEFUL | How do Git branches map to development, QA, and production deployments? |
| YT-4.32 | [30:23](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1823s) | 🟢 USEFUL | Follow-up: How do Git branches map to development, QA, and production deployments? |
| YT-4.33 | [31:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1898s) | 🟢 USEFUL | Follow-up: How do Git branches map to development, QA, and production deployments? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [29:28](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1768s) one QA and all of them are working together so how do you follow your branching techniques your repository being either they foged or cloned what is the envirment what is profiling what is<br>[29:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1785s) environments that you're using everything I would like to know so when I talk about the environments uh we have different environments like feature main Dev for developers both both feature M and | A team may use feature, development, release, and production branches, with pull requests and tests before promotion. For example, a release candidate is tested in QA before deployment to production. The exact branch model varies; what's important is controlled promotion and an auditable commit. |

<a id="ic-6"></a>

## IC-6 — How would you run and scale ten microservices with Kubernetes? ⭐

⭐ **Repeated interview question:** reused **IC-6**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.34 | [31:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1913s) | 🟢 USEFUL | How are Docker images deployed through Amazon EKS? |
| YT-4.35 | [33:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1984s) | 🟢 USEFUL | Follow-up: How are Docker images deployed through Amazon EKS? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [32:09](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1929s) create a Docker file once the docker file is done uh it will create an image from the image uh it will pick the all the particular dependencies from a container registry okay uh all the all the images<br>[32:23](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1943s) will be stored in the container registry and from the container registry it will be creating an uh I mean we are following kubernetes as of now so it will be moved to the kubernetes instance of of | A build pipeline creates a container image, pushes it to a registry, and updates a Kubernetes Deployment manifest or image reference. EKS schedules the pods and reconciles the desired replicas. For example, deploying three order pods uses one versioned image and a Deployment. EKS manages orchestration; it does not build the Java code for you. |

<a id="ic-22"></a>

## IC-22 — How do Kubernetes Services handle changing pod IP addresses?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.36 | [33:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2012s) | 🟢 USEFUL | How do Kubernetes Services handle changing pod IP addresses? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [33:47](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2027s) again a new IP address is assigned so how will a know that b which was earlier alive was crashed is alive again is having a Dynamic IP how will it interact now directly it will not uh communicate<br>[34:03](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2043s) with the container there is a concept of uh node so inside nodes uh the particular containers will run okay I mean pods inside pod pods containers will run and pod will be | Pods can restart with new IP addresses, so clients should reach them through a Kubernetes Service or another stable discovery mechanism. For example, a payment service keeps a stable DNS name even as its pods move between nodes. Kubernetes updates backend endpoints rather than requiring clients to learn every pod IP. |

<a id="is-20"></a>

## IS-20 — What changed when moving to Spring Boot 3?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.37 | [34:56](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2096s) | 🟢 USEFUL | What changed when moving to Spring Boot 3? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:13](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2113s) version of java and since it is using spring board 3 uh it is using spring six spring framework six and some of the dependencies they have moved from uh Jakarta e version I mean Java X2 Jakarta<br>[35:30](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2130s) e version and also they have come up with the concepts of observability and micrometer and also spring Cloud na basically in order to provide lightweight executable files and such | Spring Boot 3 requires Java 17 or later and uses Jakarta EE namespaces rather than older javax APIs for relevant enterprise packages. For example, older servlet imports may need changes during migration. Dependencies and framework versions also need compatibility checks. I'd plan it as a migration, not just change one version number. |

<a id="is-21"></a>

## IS-21 — How can you replace embedded Tomcat in a Spring Boot application?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.38 | [36:20](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2180s) | 🟢 USEFUL | How can you replace embedded Tomcat in a Spring Boot application? |
| YT-4.39 | [37:31](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2251s) | 🟢 USEFUL | Follow-up: How can you replace embedded Tomcat in a Spring Boot application? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [36:37](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2197s) dependency okay after excluding you have to add the dependency okay dependency yeah first you need to exclude because this is the default server right so you need to exclude that and add the<br>[36:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2210s) jend uh any profiling you have done in your application spring profiling uh you'll not have only one particular environment right you'll be having Dev QA prod So based on each and every | Spring Boot's web starter commonly uses embedded Tomcat, but compatible alternatives such as Jetty or Undertow can be configured by changing starter dependencies. For example, a team may exclude Tomcat and add the Jetty starter. I'd test servlet compatibility and deployment behavior. The HTTP server is a dependency choice, not hardcoded in controllers. |

<a id="ij-156"></a>

## IJ-156 — How do you implement a lazy Singleton safely in multithreaded Java? ⭐

⭐ **Repeated interview question:** reused **IJ-156**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.40 | [38:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2321s) | 🟢 USEFUL | How do you implement a lazy Singleton safely in multithreaded Java? |
| YT-4.41 | [39:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2390s) | 🟢 USEFUL | Follow-up: How do you implement a lazy Singleton safely in multithreaded Java? |
| YT-4.42 | [41:01](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2461s) | 🟢 USEFUL | Follow-up: How do you implement a lazy Singleton safely in multithreaded Java? |
| YT-4.43 | [42:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2534s) | 🟢 USEFUL | Follow-up: How do you implement a lazy Singleton safely in multithreaded Java? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [38:55](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2335s) chance to work with Observer command iterator and State Design patterns nice uh okay so can you tell me why you have used Singleton single ton when we talk about it is for creation it is one of the<br>[39:12](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2352s) creational design pattern only one particular instance of the class should be existing mainly we use this particular design pattern in case of logging or when we want to Cache any any | A naive check-then-create Singleton can create more than one instance when two threads race. I prefer an enum singleton or initialization-on-demand holder. If using double-checked locking, the instance field needs volatile. For example, two concurrent requests must still receive the same object. Thread safety is part of Singleton correctness. |

<a id="is-22"></a>

## IS-22 — What are singleton, prototype, request, and session bean scopes? ⭐

⭐ **Repeated interview question:** reused **IS-22**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.44 | [43:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2591s) | 🟢 USEFUL | What are singleton, prototype, request, and session bean scopes? |
| YT-4.45 | [44:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2658s) | 🟢 USEFUL | Follow-up: What are singleton, prototype, request, and session bean scopes? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [43:27](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2607s) um so this is the default scope uh if even if you're not mentioning it um only one particular instance of The Bean uh is being created in the spring container and the same instance is written<br>[43:39](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2619s) whenever the bean is being requested and all the subsequent request for that particular Bean will receive the same object reference since you are calling the same Bean again and again and in | Singleton is Spring's default bean scope and gives one instance per container and bean definition. Prototype gives a new instance when requested, request scope follows an HTTP request, and session scope follows a web session. For example, an application service is usually singleton while request-specific state must not be stored there. |

<a id="is-23"></a>

## IS-23 — Can changing a singleton Spring bean affect different consumers?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.46 | [45:18](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2718s) | 🟢 USEFUL | Can changing a singleton Spring bean affect different consumers? |
| YT-4.47 | [46:30](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2790s) | 🟢 USEFUL | Follow-up: Can changing a singleton Spring bean affect different consumers? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [45:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2733s) visible to all the other classes where it is being autoed can you repeat okay uh I have a class uh it has a attribute called his name I'm setting that particular to W<br>[45:46](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2746s) sheet now uh I'm changing that name uh to XY Z so will that beam which is Auto in different classes can see the effect of this change no since you're making the scope | If the same mutable singleton bean is injected into two services, both see changes to its shared state. For example, storing the currently logged-in user's name in a singleton field can leak information across requests. I keep application services stateless or use properly scoped state. The main lesson is that singleton does not mean thread-safe. |

<a id="ij-157"></a>

## IJ-157 — How is a classic Java Singleton different from a Spring singleton bean?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.48 | [47:40](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2860s) | 🟢 USEFUL | How is a classic Java Singleton different from a Spring singleton bean? |
| YT-4.49 | [48:54](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2934s) | 🟢 USEFUL | Follow-up: How is a classic Java Singleton different from a Spring singleton bean? |
| YT-4.50 | [50:16](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3016s) | 🟢 USEFUL | Follow-up: How is a classic Java Singleton different from a Spring singleton bean? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [47:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2873s) different from a Singleton in Spring you need to write your own logic in case of spr when you are writing only Java based applications but in case of spring only annotation is sufficient so<br>[48:11](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=2891s) automatically spring configures all the single ter so you have to put I think at scope you can no no no automatically spring manages the single T scope in uh spring | A Java Singleton implementation decides how one instance is managed, often for one class loader. Spring's singleton scope gives one bean instance per bean definition within one application context. For example, two separate Spring contexts can each create their own service singleton. They do not promise one global instance across every JVM. |

<a id="it-6"></a>

## IT-6 — How do behavior-driven tests differ from test-driven development?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.51 | [50:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3033s) | 🟢 USEFUL | How do behavior-driven tests differ from test-driven development? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [50:51](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3051s) and the tester sits and understand all the senior of a particular feature here and we use cucumba framework uh to write the bdd files in ging language so it's nothing but when given when then we need<br>[51:06](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3066s) to write all the three scenarios I mean all the scenarios uh using this particular framework and once all the three persons uh they have understood all the scenarios the developer will | TDD starts with a failing automated test, then implements the simplest code to pass it and refactors. BDD focuses on behavior described in business-readable examples. For example, a withdrawal scenario says a balance must not become negative. Both can complement each other, but they are not the same process. |

<a id="it-2"></a>

## IT-2 — How do JUnit tests and mocks isolate logic from databases and other services? ⭐

⭐ **Repeated interview question:** reused **IT-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.52 | [51:47](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3107s) | 🟢 USEFUL | How does Mockito isolate a service class from database calls? |
| YT-4.53 | [53:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3184s) | 🟢 USEFUL | Follow-up: How does Mockito isolate a service class from database calls? |
| YT-4.54 | [54:12](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3252s) | 🟢 USEFUL | Follow-up: How does Mockito isolate a service class from database calls? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [52:10](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3130s) uh all the classes which are required we'll be mocking them using at Mock Bean for example uh I'm using any service class I I should mock them and the data which I'm getting from the<br>[52:25](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3145s) repository layer I'll not be uh able to get directly from the database right I should not hit the database directly I I should not save anything directly to the database when I'm uh calling the test | Mockito can replace a repository with a mock while I test real service logic. For example, I make a mocked repository return a customer and verify the service calculates the right discount. This keeps the unit test fast and independent of a real database. Separate integration tests still verify actual persistence behavior. |

<a id="it-7"></a>

## IT-7 — What do JUnit 5 @BeforeEach and @BeforeAll do?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.55 | [54:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3266s) | 🟢 USEFUL | What do JUnit 5 @BeforeEach and @BeforeAll do? |
| YT-4.56 | [55:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3341s) | 🟢 USEFUL | Follow-up: What do JUnit 5 @BeforeEach and @BeforeAll do? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3281s) all at before each before calling any test class uh test method this particular method will be called setup method which is annotated with at before which will be called and at before all<br>[54:54](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3294s) will be called at the start of executing all the methods all the test class methods okay so you mean to say before each is Method level before each method it is called | @BeforeEach runs before every test method and can create fresh objects. @BeforeAll normally runs once before all tests in a test class and is useful for shared expensive setup. For example, each test can get a clean shopping cart. Cleanup is handled by @AfterEach and @AfterAll. Isolation matters more than saving a few setup lines. |

<a id="ia-34"></a>

## IA-34 — What does the SOLID single-responsibility principle mean? ⭐

⭐ **Repeated interview question:** reused **IA-34**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.57 | [56:08](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3368s) | 🟢 USEFUL | What does the SOLID single-responsibility principle mean? |
| YT-4.58 | [57:23](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3443s) | 🟢 USEFUL | Follow-up: What does the SOLID single-responsibility principle mean? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [56:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3381s) time example how you are working with solid principles and implementing that in your uh solid principles these are very important concept of uh while developing any code so s stands for single<br>[56:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3393s) responsibility principle basically it states that every class should have only one particular functionality and implementation of all multiple functionalities in a single | A class should have one main reason to change. For example, calculating an invoice and emailing it are separate responsibilities, so I might use an InvoiceCalculator and NotificationService. That makes changes easier to test. It doesn't mean every class can have only one method; it means one focused purpose. |

<a id="ia-35"></a>

## IA-35 — How does the open-closed principle apply to payment integrations? ⭐

⭐ **Repeated interview question:** reused **IA-35**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.59 | [58:17](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3497s) | 🟢 USEFUL | How does the open-closed principle apply to payment integrations? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [58:33](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3513s) anywhere you have used open close principle anywhere for example I'm having some logic uh for example I'm building any payment Gateway systems in my application uh currently I'm having<br>[58:47](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3527s) credit card and debit card and I I have PayPal uh after that I want to implement any other payment Gateway system which was introduced my code should be such that it should be | A component should be open to adding behavior without repeatedly editing existing stable logic. For example, implementing a PaymentMethod interface lets me add a wallet payment without changing checkout's selection flow. It reduces regression risk. The goal is practical extensibility, not avoiding every code change. |

<a id="is-24"></a>

## IS-24 — How do JPA derived queries and @Query compare? ⭐

⭐ **Repeated interview question:** reused **IS-24**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.60 | [59:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3566s) | 🟢 USEFUL | How do JPA derived queries and @Query compare? |
| YT-4.61 | [1:00:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3641s) | 🟢 USEFUL | Follow-up: How do JPA derived queries and @Query compare? |
| YT-4.62 | [1:01:59](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3719s) | 🟢 USEFUL | Follow-up: How do JPA derived queries and @Query compare? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [59:42](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3582s) for connecting the DS with jpa and what is jpa jpa is nothing but uh Java persistence API okay and uh it is connecting it is for connecting to the databases it is similar to one omm tool<br>[1:00:01](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3601s) object relation mapping okay so you you should connect to the database previously there was a concept of jdbc and it's the responsibility of developer there will | Spring Data JPA can derive queries from repository method names for simple filters. For complex joins or projections, @Query can supply JPQL or a native SQL query. For example, findByStatus handles a basic lookup, while a reporting query may need a custom join. I choose the simplest option that remains readable. |

<a id="ij-158"></a>

## IJ-158 — Why must JPA repository ID types use wrapper types?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.63 | [1:02:55](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3775s) | 🟢 USEFUL | Why must JPA repository ID types use wrapper types? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:03:28](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3808s) object are not allowed there since they using object we need to use integer there yes per correct uh now uh you you you have an application okay what is happening in your current application is | JpaRepository&lt;Entity, IdType&gt; uses generic type parameters, which require reference types. For example, a repository for an entity with an int ID generally declares Integer, not int. Java generics cannot use primitive type arguments directly. The wrapper type represents the identifier consistently in the repository API. |

<a id="id-1"></a>

## ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table? ⭐

⭐ **Repeated interview question:** reused **ID-1**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.64 | [1:03:43](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3823s) | 🟢 USEFUL | How would you diagnose a slow database query in production? |
| YT-4.65 | [1:04:51](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3891s) | 🟢 USEFUL | Follow-up: How would you diagnose a slow database query in production? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:03:55](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3835s) scenario I'll check the logs to understand which particular method is taking long time okay based on the logs I'll be understanding which particular query is taking long time perfect I'll<br>[1:04:07](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3847s) go to that particular table I'll understand how much data is available right now okay if indexing is required I need to index the table and even if even if even this is taking time I need to | I measure where the time goes, inspect an execution plan, and check indexes, joins, filtering, and table statistics. For example, searching a million orders without a useful index can force an expensive scan. I compare before-and-after latency instead of guessing. Scaling hardware is not my first step. |

<a id="ij-159"></a>

## IJ-159 — When are parallel threads a poor substitute for query optimization?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.66 | [1:05:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3900s) | 🟢 USEFUL | When are parallel threads a poor substitute for query optimization? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:05:13](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3913s) you know about shredding how do you do it how many types of shredding is there uh can you repeat strategy Str how do you do the strategy so in in case of databases uh there is a<br>[1:05:27](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3927s) concept of sharding which is nothing but you'll be dividing your data into more than one particular uh physical databases okay uh there are basically two types of uh sharding uh basically | Adding threads can increase throughput for independent work, but it won't magically fix a slow SQL plan. For example, running ten copies of a full table scan may overload the database. I'd optimize the query first and use a bounded pool only when tasks can safely run concurrently. Concurrency should remove a bottleneck, not multiply it. |

<a id="id-2"></a>

## ID-2 — Explain table partitioning versus database sharding. ⭐

⭐ **Repeated interview question:** reused **ID-2**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.67 | [1:05:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3957s) | 🟢 USEFUL | What is horizontal and vertical database partitioning? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:06:22](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3982s) want to store three columns in one table and two other columns in another table so this is based up basically ver vertical partitioning and in case of horizontal partitioning for example I<br>[1:06:34](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3994s) have 10,000 records I want to store 5,000 records in one table second 5,000 records in another table this is called as horizontal partition so basically with rows that's | Horizontal partitioning splits rows by a key, while vertical partitioning separates columns or related groups of fields. Sharding distributes subsets across database nodes. For example, order rows may be partitioned by month, while cold profile attributes can live separately. I choose a partition key based on access patterns and data growth. |

<a id="is-25"></a>

## IS-25 — How do you model a many-to-many JPA relationship?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.68 | [1:07:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4041s) | 🟢 USEFUL | How do you model a many-to-many JPA relationship? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:07:39](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4059s) table common records or the unique memory Keys unique records I mean unique unique memory keys of both the tables for example ID in both the tables oh uh uh okay I can see you have used<br>[1:07:56](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4076s) Kafka also yeah uh as we are using uh currently is a um small microservices uh pattern We are following so it's choreography design pattern we are using So based on the request of uh based on | A many-to-many relationship uses an association table linking rows from two entities. For example, students can enroll in several courses, and each course can contain several students. In JPA, @ManyToMany with @JoinTable can map the relationship, but an explicit enrollment entity is often better if the link itself has attributes. |

<a id="ia-36"></a>

## IA-36 — What are Kafka topics, partitions, and consumer groups?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.69 | [1:08:27](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4107s) | 🟢 USEFUL | What are Kafka topics, partitions, and consumer groups? |
| YT-4.70 | [1:09:34](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4174s) | 🟢 USEFUL | Follow-up: What are Kafka topics, partitions, and consumer groups? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:08:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4121s) subscribers uh any clue about the architecture of Kafka so basically when I talk about Kafka uh you have partition concept so you have have different types of partition and inside partition you have<br>[1:08:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4137s) different types of basically one is uh broker and inside broker uh you'll be having different types of topics inside topics you'll be having different types of partitions okay for for example uh for | A Kafka topic stores records in partitions, and consumers in the same group divide those partitions among themselves. For example, an order-events topic with three partitions can be processed in parallel by up to three active group members. Ordering is guaranteed within a partition, not across the whole topic. |

<a id="is-4"></a>

## IS-4 — What information must not be stored in JWT claims, and why? ⭐

⭐ **Repeated interview question:** reused **IS-4**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.71 | [1:10:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4245s) | 🟢 USEFUL | How are JWT claims different from encrypted confidential data? |
| YT-4.72 | [1:11:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4310s) | 🟢 USEFUL | Follow-up: How are JWT claims different from encrypted confidential data? |
| YT-4.73 | [1:13:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4380s) | 🟢 USEFUL | Follow-up: How are JWT claims different from encrypted confidential data? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:10:58](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4258s) implementation in your project uh I have used uh JWT JWT is nothing but Json web token so once the token is being uh created uh based on the response I mean we'll be having also expiry time so once<br>[1:11:16](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4276s) the expiry time is expired like uh of that particular token again a new token will be generated okay and so inside the Json the J toen consist of three particular parameters one is the header | A normal signed JWT exposes readable claims after Base64URL decoding. For example, a subject identifier and role may be acceptable, but a password must never be placed in the token. The signature gives integrity, not confidentiality. When an API needs private data it should retrieve it through authorization-checked backend services. |

<a id="is-26"></a>

## IS-26 — How would you configure CORS for a Spring Boot API? ⭐

⭐ **Repeated interview question:** reused **IS-26**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.74 | [1:13:29](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4409s) | 🟢 USEFUL | How would you configure CORS for a Spring Boot API? |
| YT-4.75 | [1:14:40](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4480s) | 🟢 USEFUL | Follow-up: How would you configure CORS for a Spring Boot API? |
| YT-4.76 | [1:15:49](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4549s) | 🟢 USEFUL | Follow-up: How would you configure CORS for a Spring Boot API? |
| YT-4.77 | [1:17:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4624s) | 🟢 USEFUL | Follow-up: How would you configure CORS for a Spring Boot API? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:13:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4425s) can have uh custom values as well but I'm not sure whether you can have password inside the claims okay and uh how do you handle the course issue have you faced the course C<br>[1:14:02](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4442s) is cross or sharing issue in your application connecting front to back how do you resolve it so back end will be running in one particular server and front end will be | CORS tells a browser which origins may read cross-origin responses. For example, a frontend at one domain can call an API at another when the server explicitly allows its origin and methods. It is a browser rule, not API authentication. I restrict origins and credentials carefully rather than allow everything by default. |

<a id="ic-4"></a>

## IC-4 — Explain CI versus continuous delivery and deployment, including automated gates. ⭐

⭐ **Repeated interview question:** reused **IC-4**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.78 | [1:17:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4652s) | 🟢 USEFUL | What checks should run before a service is deployed to production? |
| YT-4.79 | [1:18:42](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4722s) | 🟢 USEFUL | Follow-up: What checks should run before a service is deployed to production? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:17:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4665s) different okay so once uh all the all the four stages passed you'll be creating a merge request to that particular envir onment you want to push so then then next CD pipeline will start<br>[1:17:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4677s) so again the four stages will be common uh integration test unit test case Sona code coverage and then publish and then deploy okay okay and you deploy using any particular deployment | I'd require a build, tests, static quality checks, security scanning, and release verification before promotion. For example, a failing unit test or vulnerability gate should stop a deployment. Different organizations use different tools, but the important requirement is consistent evidence that the release is ready. |

<a id="ia-20"></a>

## IA-20 — How would you diagnose Kafka consumer lag in a distributed system? ⭐

⭐ **Repeated interview question:** reused **IA-20**. Each source video keeps its own transcript and timestamps.

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.80 | [1:19:14](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4754s) | 🟢 USEFUL | How do you investigate Kafka consumer lag and partition bottlenecks? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:19:27](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4767s) it so Kafka has a lot of things into it so you can uh yeah uh just have a look like how the architecture works because zookeeper is also there who who handles the leaders Brokers the only thing I can<br>[1:19:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4781s) find in the whole interview which is problematic is kakka apart from that uh okay for three years of experience you were good you were perfect so very nice interview no no uh | I compare consumer offsets with the newest topic offsets, check whether consumers are healthy, and inspect processing latency and partition distribution. For example, one slow partition can leave a consumer group behind even with free consumers. I fix the bottleneck or scale partitions and consumers carefully, remembering partition ordering. |
