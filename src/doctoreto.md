# [doctoreto | دکترتو](https://doctoreto.com/)

### Status
#### 📜📞🔧❌

## Senior Back-End Developer (Golang)

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> ti(Technical Interview) --rejected--x hri(HR Interview) -.-> o(Offer)
```

### Apply Way
Jobinja & Jobvision

### Interview Date

- **Sent Resume**<br />1404.04.09

- **HR Call**<br />1404.04.10

- **Technical Interview**<br />1404.04.11

- **Rejection Email**<br />1404.04.23

### Interview Duration
- **Technical Interview**<br />1 hour

### Interview Platform
Google Meet

### Technical Interview
- Tell me about the main challenges you faced in your recent roles.

- Describe a time when a component (for example, a matching engine) crashed or showed inconsistent behavior involving a message broker. How did you diagnose the problem, fix it, and ensure no data was lost?

- What mechanisms do you use to make message processing resilient?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    <a href="https://microservices.io/patterns/data/transactional-outbox.html" target="_blank" rel="noopener noreferrer">Transactional outbox</a><br />
    </div>
    </details><br />

- How did you implement the transactional outbox pattern in your system? Explain how it works and how it guarantees reliable message delivery and data consistency.

 - Do you have experience with database operations such as backups, replication, clustering, failover, and recovery?

- Which monitoring and observability tools have you used (metrics, tracing, logs)? Describe how you use them to find and diagnose bugs.

- When you work with logging, what things do you consider important and what best practices do you use?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Priorities: signal-to-noise (avoid spammy logs), structured logs (JSON), consistent schema, correlation/request IDs, accurate timestamps, proper log levels, redact sensitive data, centralized collection, retention & sampling, and cheap canonical log lines for each request.
    <a href="https://www.elastic.co/observability-labs/blog/best-practices-logging" target="_blank" rel="noopener noreferrer">elastic</a><br />
    </div>
    </details><br />

- What is eventual consistency in the context of databases and distributed systems?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    a replication model where updates will propagate and replicas converge eventually (if no new updates), so reads may be stale briefly but become consistent over time. Practical trade-off: higher availability and latency at the cost of short-term anomalies.
    <a href="https://en.wikipedia.org/wiki/Eventual_consistency" target="_blank" rel="noopener noreferrer">Wikipedia</a><br />
    </div>
    </details><br />

- What is consistency?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    In database systems, consistency (or correctness) refers to the requirement that any given database transaction must change affected data only in allowed ways. Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof. 
    <a href="https://en.wikipedia.org/wiki/Consistency_(database_systems)" target="_blank" rel="noopener noreferrer">Wikipedia</a><br />
    </div>
    </details><br />

- Which tools and mechanisms help keep a system consistent?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Common techniques: distributed consensus (Raft/Paxos), transactional guarantees (ACID), two-phase commit, idempotency + deduplication, transactional outbox and ...
    </div>
    </details><br />

- Can you list and explain common database isolation levels and the trade-offs between them?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    <a href="https://www.geeksforgeeks.org/transaction-isolation-levels-dbms/" target="_blank" rel="noopener noreferrer">geeksforgeeks</a><br />
    <a href="https://en.wikipedia.org/wiki/Isolation_(database_systems)" target="_blank" rel="noopener noreferrer">Wikipedia</a><br />
    </div>
    </details><br />

- Have you taken a course or done projects on concurrent/parallel systems?

- Is there a semaphore concept in Go?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Go has no built-in semaphore type, but a counting semaphore is commonly implemented with a buffered channel or a small wrapper around sync primitives. sync provides low-level primitives; higher-level concurrency is often done with channels.
    </div>
    </details><br />

- If you had to implement Go channels from scratch, how would you design them?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    <a href="https://medium.com/womenintechnology/exploring-the-internals-of-channels-in-go-f01ac6e884dc" target="_blank" rel="noopener noreferrer">medium</a><br />
    </div>
    </details><br />

- How are goroutines blocked and woken up? Who handles that?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    The Go runtime scheduler handles blocking/wakeup. Goroutines are parked when they wait on channels, locks, I/O, timers, or syscalls; the runtime keeps them on wait lists and moves them to runnable queues when the event occurs (timer, channel ready, I/O complete), then schedules them onto OS threads.
    </div>
    </details><br />

- How many goroutines can you create(open)?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Millions are possible, limited by memory (heap + per-goroutine stack) and scheduling overhead. GOMAXPROCS controls parallel workers/OS threads (parallelism), not the total goroutine count. Real limit depends on your workload and memory profile.
    <a href="https://www.ardanlabs.com/blog/2014/01/concurrency-goroutines-and-gomaxprocs.html" target="_blank" rel="noopener noreferrer">ardanlabs</a><br />
    </div>
    </details><br />

- Have you heard the term garbage collection pressure? What causes it and when does the GC react?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Yes. GC pressure = conditions that make the garbage collector run frequently or do much work (many short-lived allocations, large heap growth, many reachable objects). The runtime triggers GC based on heap growth/threshold heuristics; more allocations → faster heap growth → earlier collections.
    <a href="https://go.dev/blog/greenteagc" target="_blank" rel="noopener noreferrer">godev</a><br />
    </div>
    </details><br />

- How can you reduce GC pressure in Go?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Reduce allocations and object lifetimes: reuse buffers, pool temporary objects, use sync.Pool for short-lived objects, avoid unnecessary boxing/heap escapes, prefer stack/value types when safe, batch work to reuse memory. Measure with pprof and trace before optimizing.
    <a href="https://victoriametrics.com/blog/go-sync-pool/" target="_blank" rel="noopener noreferrer">victoriametrics</a><br />
    </div>
    </details><br />

- Have you used object pools such as `sync.Pool`?

- What are the main benefits of `gRPC`?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    High performance (HTTP/2 multiplexing), low latency, built-in streaming (client/server/bi-directional), strongly typed contracts via protobuf and code generation, language polyglot support, and built-in interception hooks (auth, load–balancing). Good for microservices and low-latency RPCs.
    </div>
    </details><br />

- Any questions?

<p dir="rtl">
 بیشتر سوالا از رزومه‌م بود و کارهایی که کرده بودم.
</p>

### Score
<h4><mark style="background-color:#ff9800; color:#ffffff; padding:4px 8px; border-radius:4px">7.5/10</mark></h4>
<p dir="rtl">
مصاحبه خوبی بود و مصاحبه‌کننده بسیار مودب و باتجربه بود. ردفلگی ندیدم. انتظار رفتن به مرحله بعد رو داشتم.
</p>

