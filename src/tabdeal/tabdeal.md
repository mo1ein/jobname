# [Tabdeal](https://tabdeal.org/)

### Status
#### 📜📞🔧task

### Interview process
```mermaid
flowchart LR
    sr(Send resume) --> hr(HR call) --> ti(Technical Interview I) --> task(Task)--> ti2(Technical Interview II) --> hr2(HR Interview)--> o(Offer)
```

### Apply Way
jobinja

### Interview Date

- **Sent Resume**<br />1405.00.00

- **HR Call**<br />1405.07.28

- **Technical Interview**<br />1405.03.30

### Interview Duration
- **Technical Interview**<br />1 hour

### Interview Platform
Google Meet

### Technical Interview

- Tell me about yourself.

- What is your most challenging experience that you involved with in your work?

- What you gonna do if suddenly we recieve massive requests? How you can handle it?

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

    ### 1. 🎯 Short Answer

    First, I'd identify the bottleneck — is it CPU, memory, DB, or network? Then apply a layered approach: add caching (Redis) to reduce DB hits, scale horizontally with load balancers, use rate limiting to protect upstream services, and offload heavy work to async queues (Kafka/RabbitMQ) so the main path stays fast.

    ### 1. 🎯 Long Answer

    When facing a sudden traffic spike, the key is to respond in layers rather than panic-fixing one thing. Start by observing metrics (latency, error rates, CPU, memory, DB connections) to pinpoint the bottleneck. If the bottleneck is the database, introduce caching layers like Redis or CDN for read-heavy data. If it's compute, scale horizontally by adding more instances behind a load balancer. If the issue is synchronous processing overwhelming your system, decouple with message queues — push non-critical work (notifications, analytics) to background consumers. Apply rate limiting and circuit breakers to prevent cascading failures. Finally, consider auto-scaling policies so the system adapts proactively to traffic patterns.

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

- One service sent events to other service and retries it and we have 3 events in destination service how can handle it in second service? for example 3 same events of buy order.
the answer is we check with uuid or request id ...

  <details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px; background-color: rgba(74,85,104,0.15);">

    ### 1. 🎯 Short Answer

    This is the **idempotency** problem. The solution is to assign a unique ID (UUID or request ID) to each event and have the receiving service track processed IDs. When a duplicate arrives, the service checks the ID, sees it's already processed, and ignores it. This ensures that processing an event multiple times has the same effect as processing it once.

    ### 1. 🎯 Long Answer

    In distributed systems, networks are unreliable. The producer service might retry sending an event because it didn't receive an acknowledgment, even though the consumer already processed it. This leads to duplicate processing. The standard solution is **idempotent processing**: attach a unique identifier (UUID, request ID, or a composite key like order_id + event_type) to each event. The consumer stores processed IDs in a fast lookup (Redis or database) with a TTL. On each incoming event, it first checks if the ID exists — if yes, it returns success without reprocessing; if no, it processes the event and stores the ID atomically. For database operations, you can also use unique constraints or upserts as a safety net.

    ### 2. 💡 Illustration / Analogy

    It's like a ticket at a concert. Each ticket has a unique barcode. When you scan it at the entrance, the system marks it as "used." If you try to scan the same ticket again (or someone copies it), the system sees it's already been used and denies entry — even though the ticket looks valid.

    ### 3. 🛠️ Real-World Example

    In a crypto exchange, when a buy order event is published to the trade matching service, we attach an `event_id` (UUID v4). The matching service stores processed event IDs in Redis with a 24-hour TTL:

    ```python
    # Pseudocode
    def process_event(event):
        idempotency_key = f"event:{event.event_id}"
        if redis.set(idempotency_key, "1", nx=True, ex=86400):
            # First time — process it
            execute_trade(event.order)
            return "processed"
        else:
            # Duplicate — skip
            return "already_processed"
    ```

    For extra safety, the database has a unique constraint on `(order_id, event_type)` so even if Redis is down, duplicates can't create double trades.

    ### 5. 🎤 Interview Tips

    **Common follow-up questions:**
    - What happens if Redis crashes and we lose the idempotency keys?
    - How do you choose the TTL for idempotency keys?
    - What's the difference between exactly-once and effectively-once delivery?
    - How does Kafka handle this differently from RabbitMQ?

    **Common mistakes candidates make:**
    - Not thinking about the atomicity of "check ID + process + store ID"
    - Forgetting edge cases like Redis failure between check and store
    - Confusing idempotency with deduplication (they're related but not identical)

    **What interviewers are looking for:**
    - Immediate recognition of the idempotency pattern
    - Understanding of the atomicity requirement
    - Awareness of failure modes and defense-in-depth (Redis + DB constraint)

    </div>
    </details>

- When do you use queue?

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

### Task

### HR Interview

### Score

