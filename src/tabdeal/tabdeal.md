# [Tabdeal](https://tabdeal.org/)

### Status
#### 📜📞🔧📝❌

### Interview process
```mermaid
flowchart LR
    sr(Send resume) --> hr(HR call) --> ti(Technical Interview I) --> task(Task)--> ti2(Task Review) --rejected--x hr2(HR Interview) -.-> o(Offer)
```

### Apply Way
jobinja

### Interview Date

- **Sent Resume**<br />1405.03.15

- **HR Call**<br />1405.02.27

- **Technical Interview**<br />1405.03.30

- **Task**<br />1405.03.31

- **Task Interview**<br />1405.04.06

### Interview Duration

- **Technical Interview**<br />1 hour

- **Task**<br />5 days

- **Task Review**<br />1 hour

### Interview Platform
Google Meet

### Technical Interview

- Tell me about yourself.

- What is your most challenging experience that you involved with in your work?

- What would you do if suddenly we receive massive requests? How would you handle it?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  If we suddenly receive a massive number of requests, the first thing I'd do is identify the root cause instead of immediately scaling the system. I'd check our monitoring dashboards, logs, and traces to understand whether the spike is caused by legitimate user traffic, a recent deployment, a client bug causing excessive retries, or even malicious traffic.

  Next, I'd identify the bottleneck by looking at metrics such as request latency, error rates, CPU and memory usage, database performance, connection pool utilization, and network traffic.

  Once I know the bottleneck, I'd apply the appropriate solution:

  - If the database is overloaded, I'd reduce the load with Redis or CDN caching, optimize slow queries, or use read replicas for read-heavy workloads.
  - If the application servers are the bottleneck, I'd scale them horizontally behind a load balancer or rely on auto-scaling if it's configured.
  - If synchronous processing is slowing requests, I'd move non-critical tasks like notifications or analytics to background workers using a message queue.
  - To protect the system from cascading failures, I'd enable rate limiting, circuit breakers, and, if necessary, load shedding.

  After the incident is resolved, I'd perform a postmortem to understand what happened, fix the root cause if it was a bug, review our auto-scaling and capacity planning, and run load tests to ensure we're better prepared for future traffic spikes.  

  </div>
  </details>

- What is Consistency?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    In **database systems (ACID)**, consistency (or correctness) refers to the requirement that any given database transaction must change affected data only in allowed ways. Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof.
  <a href="https://en.wikipedia.org/wiki/Consistency_(database_systems)" target="_blank" rel="noopener noreferrer">Wikipedia</a><br />

    In **CAP** theorem:
    Every read receives the most recent write or an error. Consistency means that all clients see the same data at the same time, no matter which node they connect to. For this to happen, whenever data is written to one node, it must be instantly forwarded or replicated to all the other nodes in the system before the write is deemed ‘successful’
  <a href="https://en.wikipedia.org/wiki/CAP_theorem#:~:text=Every%20read%20receives,%5B5%5D" target="_blank" rel="noopener noreferrer">Wikipedia</a>
  </div>
  </details>

- For displaying a user's daily Profit & Loss (P&L) in a crypto exchange system, which is more important: Consistency or Availability? Why?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  Consistency is usually more important because users expect their P&L to reflect the latest trades, balances, and market positions accurately. Showing stale or inconsistent data can lead to incorrect decisions and loss of trust. In CAP theorem terms, this feature is typically CP-oriented, prioritizing strong consistency over high availability. Techniques such as transactional updates, event ordering, and read-after-write consistency help ensure accurate PnL calculations.    
  </div>
  </details>

- What is double spending?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  **Double-spending** is the unauthorized spending of the same money (either digital or conventional) more than once. It happens when someone tries to spend the same money in multiple transactions before the first transaction is fully confirmed.

  **Example**: Alice has 1 BTC and sends it to Bob. Before the network confirms the transaction, she tries to send the same 1 BTC to Charlie. A properly designed blockchain detects the conflicting transactions and accepts only one of them, preventing the same coin from being spent twice.    
  </div>
  </details>

- One service sends events to another service and retries, resulting in 3 duplicate events at the destination service. How can the second service handle this? For example, 3 identical buy order events.
the answer is we check with uuid or request id ...

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  This is the **idempotency** problem. The solution is to assign a unique ID (UUID or request ID) to each event and have the receiving service track processed IDs. When a duplicate arrives, the service checks the ID, sees it's already processed, and ignores it. This ensures that processing an event multiple times has the same effect as processing it once.

  </div>
  </details>

- When do you use a queue?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

    Queues are used in several key scenarios: 

    (1) **Decoupling** — when the producer doesn't need to wait for the consumer to finish (e.g., sending emails after order placement); 

    (2) **Buffering** — when the producer generates work faster than the consumer can handle (e.g., flash sale orders hitting a slow payment gateway); 

    (3) **Async processing** — when a task is slow but the user needs a fast response (e.g., video transcoding, report generation); 

    (4) **Reliability** — when you need guaranteed delivery with retries and dead-letter queues (e.g., financial transactions); 

    (5) **Load leveling** — spreading work evenly over time instead of processing spikes; 

    (6) **Fan-out** — one event triggering multiple downstream services (e.g., an order event updating inventory, analytics, and notifications simultaneously).

  </div>
  </details>

- When starting a new project, do you prefer a monolithic architecture or a microservices architecture, and why?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  I usually **start with a monolith and split it into microservices when needed**. A monolith is faster to develop, easier to debug, and simpler to deploy and maintain, allowing the team to move quickly in the early stages. As the system grows and requirements such as independent scaling, team autonomy, or clear domain boundaries emerge, I gradually decompose it into microservices. This approach avoids the premature complexity of distributed systems—such as network communication, distributed transactions, and observability challenges—while keeping the architecture scalable.
  </div>
  </details>

**Math Question:**

- 8 machines in 4 hours do 8 tasks. 
- 20 machines in 10 hours do x tasks?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">
  
  \\[
  8 \times 4 = 32 \text{ machine-hours}
  \\]

  \\[
  20 \times 10 = 200 \text{ machine-hours}
  \\]

  \\[
  \frac{32}{8} = \frac{200}{x}
  \\]

  \\[
  x = \frac{200 \times 8}{32}
  \\]

  \\[
  x = 50 \text{ tasks}
  \\]
  </div>
  </details>

#### Live code

- Implement an LRU Cache in 20 mins.

  <details>
  <summary style="font-size:14px"><b><em>Answer (My solution)</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

  ```python
  class LRUCache:
      def __init__(self, capacity: int) -> None:
          self.capacity = capacity
          self.cache = {}
          
      def put(self, key: int, value: int):
          if key in self.cache:
              self.cache[key] = value
              self.cache[key] = self.cache.pop(key)
          else:
              if len(self.cache) == self.capacity:
                  del self.cache[next(iter(self.cache))]
              self.cache[key] = value

      def get(self, key: int):
          if key not in self.cache:
              return -1
          self.cache[key] = self.cache.pop(key)
          return self.cache[key]

      def print_cache(self):
          print(self.cache)

  c = LRUCache(3)

  c.put(1,1)
  c.put(2,2)
  c.put(3,3)
  c.print_cache()
  c.get(2)
  c.get(1)
  c.print_cache()
  c.put(4,4)
  c.print_cache()
  ```

  </div>
  </details>

<p dir="rtl">
این مرحله همه سوالاتو جواب دادم و دیگه حرفی نمونده بود و پشمای طرف ریخته بود طوری که فرداش زنگ زدن برای مرحله بعد، اما چیزی که رو مخم بود بی‌سوادی مصاحبه‌کننده بود مثل یه ربات از رو لیست داشت سوال می‌خوند یه کوچولو هم مانور نمی‌داد رو سوالا که ببینه چقدر تو اون دامین مسلطم صرفا خبرنگاری سوال و جواب. لایوکدم که زدم متوجه نمی‌شد هی می‌گفت دیکشنری رو چی کار کردی هی توضیح می دادم آخر انقد تست کیس مختلف داد گفت آها درست کار می‌کنه! 
</p>

### Task & Code review interview

<p dir="rtl">
پس از مصاحبه فنی تسکی فرستادند که می‌تونید از
<a href="./Backend Project.pdf">این‌جا</a>
ببینید. و همین‌طور 
<a href="https://github.com/mo1ein/qq">جواب</a>
من رو.
<br />
خود نوع نگارش تسک گویای اینه که چه خبره اون تو!
مصاحبه‌کننده به شدت نوب بود و سنیوریتی لازم و سواد کافی برای سنجیدن دیگری رو نداشت فکر کنم کلا ۲-۳ سال سابقه داشت و خوب متوجه کد نشد و وب‌کم رو هم تو این مرحله روشن نکرد. صداها و مکث‌های عجیبی هم میومد انگار چند نفر پشت مانیتور باشن. طبق تحقیقات و ارتباطاتم فهمیدم که بچه‌های تیم رندوم مصاحبه می‌کنن که نشون می‌ده همین‌طوری خیاریه مصاحبه‌ها. سوال‌ها هم یه لیستیه که طوطی‌وار می‌پرسن و خب برای همه هم همونه.
</p>

### Score

<h4><mark style="background-color:#ff9800; color:#ffffff; padding:4px 8px; border-radius:4px">6/10</mark></h4>

<p dir="rtl">
رقمی بد نبود با یه عدد سه رقمی اوکی بودن یعنی اولش که HR زنگ زد گفتم انقد و گفت خب حالا خبر می‌دیم بهت، رفت با رئیسش (احتمالا) صحبت کرد بعد چند روز مصاحبه ست کردن حالا دیگه نمی‌دونم واقعا اوکی بودن یا تهش به آفر می‌رسید می‌گفتن خب ما ۵۰ بیشتر نمی‌دیم. ولی خب چون پول دارن بنا رو می‌ذاریم رو این که اوکی بودن. در هر صورت اگه فقط پول می‌خواید لقمه راحتیه ولی جای باحال، فکر نکنم!
</p>
