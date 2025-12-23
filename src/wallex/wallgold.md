# [Wallgold (Wallex)](https://wallgold.ir/)

### Status
#### 📜📞🔧👱🏻‍♀️🔧❌

## Full-Stack Developer (Backend focosed)

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> ti(Screening Interview) --> hri(HR Interview) --> ti2(Technical Interview) --rejected--x o(Offer)
```

### Apply Way
jobinja

### Interview Date

- **Sent Resume**<br />1404.06.05

- **HR Call**<br />1404.07.06

- **Screening interview**<br />1404.07.12

- **HR Interview**<br />1404.07.14

- **Technical Interview**<br />1404.07.21

- **Rejection Email**<br />1404.07.30

### Interview Duration

- **Screening interview**<br />1 hour

- **HR Interview**<br /> 30 minutes

- **Technical Interview**<br />1 hour

### Interview Platform
Google Meet

### Screening Interview 

- Tell me about yourself

- Are you a student?

- Do you have plans to migrate?

- Are you OK with full-time work??

- Are you OK with on-call?

- What are your salary expectations?

### HR Interview

- Tell me about yourself

- What is your greatest strength?

- Why do you want to leave your current company?

- What would make you consider leaving your company, even if the salary is great?

- What are your salary expectations?

### Technical Interview

- Do you now wallex?

- Tell me about yourself.

- We have a cache for some data in our exchange that we show on the page to users, such as the number of trades, Tether price, etc. When the cached data is cleared, many requests hit the database directly, causing heavy load and potential downtime. How would you fix this problem?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    #### 1. Primary Defense: The Mutex Lock with Stale Data Fallback

    This is your immediate and most critical fix. It directly stops the herd.

    **How it works**: When the cache for a key is found to be empty or expired, the first request to notice it acquires a distributed lock (e.g., in Redis). Only this request is permitted to query the database.

    **Handling Subsequent Requests**: All other concurrent requests for the same data are not sent to the database. Instead, they have two graceful paths:

    **Wait Briefly**: They can wait for a short, fixed period (e.g., 50-100ms) for the first request to populate the cache.

    **Serve Stale Data (Preferred)**: Even better, the system immediately returns the recently expired ("stale") data while the cache is being refreshed in the background. This provides the best user experience—fast responses with near-real-time data.

    #### 2. Proactive Mitigation: Prevent Synchronized Expiration

    The thundering herd is often caused by thousands of cache entries expiring at the same moment.

    **Jitter**: Never set a fixed TTL (Time-To-Live). Instead, add a small, random value (±10%) to the expiration time. This spreads cache regeneration naturally over a window of time, preventing a synchronized stampede.

    **Probabilistic Early Refresh**: Before a cache entry officially expires, have a small percentage of requests (e.g., 1%) trigger an early refresh in the background. This "warms" the cache proactively, making it highly likely that a fresh value is already in place before the true expiration time.

    #### 3. Architectural Decoupling: Asynchronous Cache Population

    For the ultimate resilience, decouple the user request from the cache regeneration process entirely.

    **How it works**: A cache miss never triggers a synchronous database call from a user request. Instead, the system always returns stale data or a default and pushes a "cache refresh task" for that key onto a background job queue (e.g., Redis Queue, SQS, Kafka).

    **Benefit**: User response times become immune to database performance. The background workers can process the refresh tasks at their own pace, and the database load is smoothed out. This is the most robust long-term pattern for high-throughput systems.
    </div>
    </details>

- Suppose we have an e-commerce product (like Digikala) and there's an issue: when I add one item to my basket, two are added. This happens sometimes. How would you fix this problem?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    #### 1. Reproduce & observe

    Reproduce in dev with different browsers/devices and slow network.

    Capture request traces (client logs, server logs, request IDs, timestamps) and check analytics for patterns (specific browsers, mobile, retries).

    #### 2. Identify likely causes

    **Client**: double-click, button not disabled, or UI retry/optimistic update doing a second call.

    **Network/client library**: automatic retry on timeout/resend.

    **Server**: non-idempotent endpoint creating two rows due to race conditions or missing uniqueness constraints.

    **Message layer**: duplicate messages processed twice.

    #### 3. Fixes (short & practical)

    **Client**: disable add button after first click and debounce UI actions; show clear loading state.

    **API**: make the operation idempotent — accept an Idempotency-Key (or request id) and store processed keys to ignore duplicates.

    **DB**: enforce correctness with a uniqueness constraint on (cart_id, product_id) and use an atomic upsert to increment quantity, e.g.

    </div>
    </details>

- Think we know the problem is from front-end and we don't want to deploy new version in front and want to fix it for short time in backend how fix it?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    #### 1. Fast dedupe/lock in cache (Redis)

    Prevent processing the same “add” twice within a short window (2–5s). Build a dedupe key from stable request factors you have today (authenticated user_id or session_id, product_id, and a hash of the request body / headers). Use SET key value NX PX <ms>.

    #### 2. Make DB operation idempotent/atomic (defensive)

    Even with Redis, races or Redis failures can happen. Enforce a DB-level uniqueness + atomic upsert so duplicates can’t create two rows.

    #### 3. Optional: Consumer-side dedupe / idempotency store

    If your API is queue-based or background-processed, store processed request IDs (or the same dedupe key) for a short TTL and ignore duplicates.

    #### 4. Response strategy & UX-friendly behavior

    When duplicate is detected in cache, return a harmless success (200) with current cart state — avoids confusing the frontend.

    If you detect duplicate after DB upsert, return the updated qty (so frontend can reconcile).

    #### 5. Observability & short-term rollout

    Add logging/metric (count of dedupe-hits, Redis failures, db-constraint triggers).

    Feature-flag the change if possible; otherwise deploy in a safe rollout.

    Monitor for false positives (legitimate rapid adds being collapsed) and tune TTL (e.g., 2–5s).

    #### 6. Caveats

    This is a short-term backend mitigation. It can merge legitimate rapid adds (user intentionally clicks twice quickly) — verify acceptable with product.

    **Long-term**: fix front-end (disable button/debounce + send idempotency key) for best UX.

    </div>
    </details>

- We have two microservices. One of them is very slow and some requests time out without receiving a response. How can the other microservice handle this to avoid being affected?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    - Set a strict downstream timeout and propagate cancellation.

    - Use a [circuit breaker](https://microservices.io/patterns/reliability/circuit-breaker.html) to fail fast after repeated timeouts.

    - Retry only idempotent calls with exponential backoff + jitter (limit attempts).

    - Apply bulkheads (separate thread/connection pools) to isolate resources.

    - Provide fallbacks or cached responses where possible.

    - If suitable, make the call async (queue + worker) to decouple user latency.

    - Add metrics/tracing and alert on downstream latency/failure rates.

    </div>
    </details>

- We have a very large, unstructured log file containing Divar chat data (ranging from gigabytes to terabytes). How would you approach detecting bot activity?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    #### 1. Data Parsing and Structuring
    **Reading File**: To read a huge file efficiently, stream it in manageable chunks (e.g., several hundred MB at a time) instead of loading it all into memory. Use memory mapping for faster access when possible, and consider distributed or parallel processing frameworks like Apache Spark if you have large-scale infrastructure. Optimize I/O by tuning buffer sizes and, if applicable, store data in compressed or columnar formats to speed selective reads. 

    **Log Parsing**: First, I'd parse the unstructured logs into a structured format (e.g., JSON or CSV) by extracting key fields such as timestamp, user ID, message content, IP address, and user agent (if available). This can be done using tools like Apache NiFi for data flow, or custom scripts with regular expressions, but for large-scale data, distributed processing is essential.

    #### 2. Feature Engineering (Bot Indicators)

    **Why**: Bots exhibit patterns like bursty activity, repetition, and anomalies vs. human behavior.
    Key Features (Computed in Spark for scale):

    - **Frequency**: Messages per sender per hour/day (bots send 100x human rates).
    - **Diversity**: Unique receivers per sender (bots spam many).
    - **Repetition**: Message similarity (e.g., Jaccard or Levenshtein distance across a user's messages).
    - **Timing**: Response latency (bots <1s), session duration (bots 24/7).
    - **Content**: Keyword scores (e.g., URLs, spam phrases like "urgent deal", "transfer money"). Use NLP for entropy (low for scripted bots).
    - **Graph**: Sender-receiver graph density (bots form hubs).
    - **Aggregates**: Group by sender_id, compute stats like avg_response_time, msg_count, unique_msgs_ratio = unique_messages / total_messages.

    </div>
    </details>

- What are your salary expectations?

- Any questions?

### Score
<h4><mark style="background-color:#4caf50; color:#ffffff; padding:4px 8px; border-radius:4px">9/10</mark></h4>

<p dir="rtl">
سوالات زیبایی پرسیده شد و نگاه مهندسی نرم‌افزار و حل مسئله داشت. به طور کلی راضی بودم منم اوکی بودم هر چند یکی از سوالا رو نتونستم خوب جواب بدم.
</p>
