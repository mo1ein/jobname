# [Zibal](https://zibal.ir/)

### Status
#### 📜📞🔧📝❌

## Senior Python Developer

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> ti(Technical Interview) --> task(Task) --rejected--x hri(HR Interview) -.-> o(Offer)
```

### Apply Way
Jobinja

### Interview Date

- **Sent Resume**<br />1404/07/15

- **HR Call**<br />1404/07/28

- **Technical Interview**<br />1404/08/03

- **Rejection Email**<br />1404/08/24

### Interview Duration
- **Technical Interview**<br />1 hour

### Interview Platform
Google Meet

### Technical Interview

- Tell me about yourself

- Do you make decisions on your team, or is there a designated decision-maker?

- Did you implement the matching engine synchronously or asynchronously? How did you handle race conditions?
    
- When you want to learn something new, what is your process (videos, docs, books, etc.)?

- What is difference between `is` and `==` in python?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    The `is` operator checks for **identity**. <br>
    The `==` operator checks for **equality**.

    ```python
    a = [1, 2, 3]
    b = a     # b references the same list as a
    c = a[:]  # c is a new list with the same content as a

    print(a is b)  # True, because b is the same object as a
    print(a is c)  # False, because c is a different object
    print(a == c)  # True, because a and c have the same content
    ```
    </div>
    </details><br />

- What is the difference between a `@classmethod` and a `@staticmethod`? When would you use a `@classmethod`?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    `@classmethod` receives the class (`cls`) and is used for alternative constructors or methods that operate on class-level state. `@staticmethod` has no implicit first argument and is used for utility functions grouped with the class without accessing class or instance state. <br />
    <a href="https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=You%20use%20a%20class%20method,class%20instances%20with%20specific%20configurations." target="_blank" rel="noopener noreferrer">realpython</a><br />
    </div>
    </details><br />

- What is a generator and what are its benefits?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    A generator is a function that yields values lazily and returns an iterator. Benefits: low memory usage for large sequences, simple stateful iteration, and easy composition of pipelines. <br />
    <a href="https://realpython.com/introduction-to-python-generators/" target="_blank" rel="noopener noreferrer">https://realpython.com/introduction-to-python-generators/</a><br />
    </div>
    </details><br />

- How do you create private methods in Python?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Use a single leading underscore `_method` to indicate ‘internal’ use (convention). Use double leading underscores `__method` for name-mangling to reduce accidental access from subclasses; note that nothing is truly private. <br />
    <a href="https://www.datacamp.com/tutorial/python-private-methods-explained" target="_blank" rel="noopener noreferrer">https://www.datacamp.com/tutorial/python-private-methods-explained</a>
    </div>
    </details><br />

- How does Django ORM address the N+1 query problem?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Django provides `select_related` for single-valued relationships and `prefetch_related` for many-to-many or reverse relations to eager-load related objects and avoid N+1 queries. You should profile queries and use `.values()` or annotations when appropriate. <br />
    <a href="https://www.youtube.com/watch?v=zwF5ADW6eKs" target="_blank" rel="noopener noreferrer">https://www.youtube.com/watch?v=zwF5ADW6eKs</a><br />
    <a href="https://docs.djangoproject.com/en/5.2/topics/db/optimization/" target="_blank" rel="noopener noreferrer">https://docs.djangoproject.com/en/5.2/topics/db/optimization/</a><br />
    <a href="https://docs.djangoproject.com/en/5.2/ref/models/querysets/" target="_blank" rel="noopener noreferrer">
    https://docs.djangoproject.com/en/5.2/ref/models/querysets/</a><br />
    </div>
    </details><br />

- Can you explain Django’s architecture?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Django follows an MTV (Model–Template–View) pattern: Models hold data/ORM; Views handle requests; Templates render presentation. Requests flow through middleware, URL routing sends them to views, which use models/templates; Django runs on WSGI/ASGI. <br />
    <a href="https://dev.to/vincenttommi/2-understanding-djangos-architecture-the-mtv-pattern-1gl" target="_blank" rel="noopener noreferrer">https://dev.to/vincenttommi/2-understanding-djangos-architecture-the-mtv-pattern-1gl</a><br />
    </div>
    </details><br />

- Describe the backend architecture you worked on and its layers.
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Microservices behind an API gateway, an auth layer, service layer (HTTP/gRPC), business/service layer, repository/data layer, and persistent stores (MySQL/Postgres, Redis). Async work is handled by message brokers and workers; observability uses logs, metrics, and tracing; deployments use Docker + Kubernetes.
    </div>
    </details><br />

- Why do we use a repository layer in a service?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    A repository abstracts persistence, centralizes queries, and decouples domain logic from storage details — making testing, swapping databases, and enforcing consistency simpler.
    </div>
    </details><br />

- What are serializers in Django REST Framework (DRF)?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Django’s serialization framework provides a mechanism for “translating” Django models into other formats. Usually these other formats will be text-based and used for sending Django data over a wire, but it’s possible for a serializer to handle any format (text-based or not).
    <a href="https://docs.djangoproject.com/en/5.2/topics/serialization/#:~:text=Django's%20serialization%20framework%20provides%20a,text%2Dbased%20or%20not)." target="_blank" rel="noopener noreferrer">djangoproject</a><br />
    </div>
    </details><br />

- What are custom permissions in DRF and how do you implement them?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Custom permissions encapsulate business authorization rules. Implement them by subclassing `rest_framework.permissions.BasePermission` and overriding `has_permission` and/or `has_object_permission`, then apply to views or viewsets. <br />
    <a href="https://www.django-rest-framework.org/api-guide/permissions/" target="_blank" rel="noopener noreferrer">https://www.django-rest-framework.org/api-guide/permissions/</a><br />
    </div>
    </details><br />

- How can you ensure only one instance of your database adapter is created in Python?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    With singleton pattern 
    </div>
    </details><br />

- How do you track requests and implement rate limiting? At which layers can this be applied?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Track requests with unique request IDs, structured logs, and distributed tracing (OpenTelemetry). Rate limiting can be applied at the edge (CDN, API gateway, reverse proxy), in a middleware layer, or in the application using token-bucket algorithms stored in Redis for shared counters.
    </div>
    </details><br />

- What’s the difference between inheritance and composition?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Inheritance models an ‘is-a’ relationship and shares behavior via a superclass. Composition models ‘has-a’ and embeds functionality by using other objects. Composition is generally preferred for flexibility and testability.
    </div>
    </details><br />

- What is dependency injection?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Dependency injection supplies an object’s dependencies from the outside (constructor, setter, or factory) rather than creating them internally; this improves testability, decoupling, and configurability.
    </div>
    </details><br />

- Which databases have you worked with?

- What does ACID stand for? 
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    <a href="https://en.wikipedia.org/wiki/ACID" target="_blank" rel="noopener noreferrer">https://en.wikipedia.org/wiki/ACID</a><br />
    </div>
    </details><br />

- What is a race condition and how can you solve it?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    A race condition happens when concurrent operations interleave and produce incorrect state. Solve it
    with mutual exclusion (mutexes) for in-process protection, transactions, locks (pessimistic or optimistic), atomic DB operations, idempotency, or by
    redesigning to avoid shared mutable state.
    </div>
    </details><br />

- How did you handle race conditions in the matching engine you worked on?

- What is the difference between a thread and a process?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Threads share a process memory space (lightweight, require synchronization). Processes have separate memory (safer isolation, heavier IPC). Choose threads for shared-memory, processes for isolation.
    </div>
    </details><br />

- How can use for example 30 core of cpu in production with python?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    In Python, you scale CPU usage by running multiple processes, not threads. In production I usually run Uvicorn behind Gunicorn and configure it with one worker per CPU core—so on a 30-core machine, -w 30 lets the app fully utilize all cores.

    ```bash
    gunicorn app:app -k uvicorn.workers.UvicornWorker -w 30
    ```
    </div>
    </details><br />

- Have you worked in production or fixed bugs in production?

- Are you familiar with Uvicorn workers?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">
    Yes — Uvicorn provides worker classes (often used with Gunicorn) to run ASGI apps across multiple
    processes; understand worker lifecycle, when to scale workers vs async concurrency, and how to
    supervise them in production.<br />
    <a href="https://www.uvicorn.org/deployment/" target="_blank" rel="noopener noreferrer">https://www.uvicorn.org/deployment/</a><br />
    <a href="https://docs.gunicorn.org/" target="_blank" rel="noopener noreferrer">https://docs.gunicorn.org/</a>
    </div>
    </details><br />


- How do you push commits to another branch?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">
    cherry-pick
    </div>
    </details><br />

### Task

<p dir="rtl">
پس از مصاحبه فنی تسکی فرستادند که می‌تونید از
<a href="./zibal_backend_project">این‌جا</a>
ببینید. و همین‌طور 
<a href="https://github.com/mo1ein/zibal">جواب</a>
من رو.
</p>

### Score
<h4><mark style="background-color:#ff9800; color:#ffffff; padding:4px 8px; border-radius:4px">6.5/10</mark></h4>

<p dir="rtl">
فرصت ۳ روزه برای این تسک کمه و تنبلی مصاحبه‌کننده در طراحی سنجش رو نشون می‌ده. نیازی به این همه بیل و کلنگ نبود. با این موضوع حال نکردم (اگر چه با مقوله تسک زدن به طور کلی حال نمی‌کنم شما وقت‌ رو می‌ذارید آیا بشود آیا نشود) از طرفی حس کردم اونقدر هم جایی نیست که بتونم چیز یاد بگیرم چون اکثر نیروهاشون جونیور بودند. فید‌بک هم که طبق معمول کسی نمی‌ده. سوالات مرحله اول خوب بود، اون قسمت‌ش رو دوست داشتم.
</p>
