# [Saraf](https://saraf.app/)

### Status
#### 📜📞🔧🔧❌

## Back-End Developer

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> si(Screening Interview) --> ti(Technical Interview) --rejected--x hri(HR Interview) -.-> o(Offer)
```

### Apply Way
Jobvision

### Interview Date

- **Sent Resume**<br />1404.07.18

- **HR Call**<br />1404.07.28

- **Screening Interview**<br />1404.07.30

- **Technical Interview**<br />1404.08.05

- **Rejection Email**<br />1404.08.12

### Interview Duration

- **Screening Interview**<br />30 minutes

- **Technical Interview**<br />1 hours

### Interview Platform
Google Meet

### Screening Interview

- Tell me about yourself.

- Explain what a race condition is in an order-matching / exchange system (for example, in a matching engine). Give concrete examples of how race conditions can occur and describe strategies you would use to prevent or resolve them.

- How would you design a system that avoids data loss when using a message broker (for example, RabbitMQ)?

### Technical Interview (Live Coding)
- We want to implement a simple token-bucket algorithm in middleware to rate-limit users?

    <details>
    <summary style="font-size:14px"><b><em>My Answer</em></b></summary>
    <a href="https://go.dev/play/p/62zP7BcAAYd">Run</a>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    ```go
    package main

    import (
        "fmt"
        "time"
    )

    type User struct {
        accountID      int64
        capacity       int64
        counter        int64
        refillRate     int64
        lastRefillTime time.Time
    }

    func handler(user User, userData map[int64]User) {
        if _, ok := userData[user.accountID]; ok {
            fmt.Println("OK")
            ud := userData[user.accountID]
            if ud.counter >= ud.capacity {
                fmt.Println(ud.counter)
                panic("rate limit reached")
            }
            ud.counter++
            fmt.Println(ud.counter)
            elapsTime := time.Now().Unix() - ud.lastRefillTime.Unix()
            ud.counter += elapsTime * ud.refillRate
        } else {
            u := User{accountID: 123, capacity: 10, counter: 0, refillRate: 1}
            userData[u.accountID] = u
        }
        fmt.Println(user.counter, " ", user.capacity, " ", user.refillRate, " ", user.lastRefillTime)
    }

    func main() {
        userData := make(map[int64]User, 0)
        newUser := User{accountID: 123, capacity: 10, counter: 0, refillRate: 1, lastRefillTime: time.Now()}
        for i := range 10 {
            fmt.Println("i:", i)
            handler(newUser, userData)
        }
    }
    ```
    </div>
    </details>
    <p dir="rtl">
    این‌جا اشتباهم این بود که مقدار map رو عوض کردم دوباره نذاشتم توش.
    </p>

    <details>
    <summary style="font-size:14px">
    <b><em><span style="background-color:#16a34a; color:#ffffff; padding:3px 8px; border-radius:6px; display:inline-block;">Answer</span></em></b>
    </summary>
    <a href="https://go.dev/play/p/E4jpxBj1B6i">Run</a>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    ```go
    package main

    import (
        "fmt"
        "sync"
        "time"
    )

    type User struct {
        accountID      int64
        capacity       int64
        tokens         int64
        refillRate     int64
        lastRefillTime time.Time
        mutex          sync.Mutex
    }

    type TokenBucketManager struct {
        users map[int64]*User
        mutex sync.RWMutex
    }

    func NewTokenBucketManager() *TokenBucketManager {
        return &TokenBucketManager{
            users: make(map[int64]*User),
        }
    }

    func (tm *TokenBucketManager) GetOrCreateUser(accountID int64, capacity, refillRate int64) *User {
        tm.mutex.Lock()
        defer tm.mutex.Unlock()

        if user, exists := tm.users[accountID]; exists {
            return user
        }

        user := &User{
            accountID:      accountID,
            capacity:       capacity,
            tokens:         capacity, // Start with full bucket
            refillRate:     refillRate,
            lastRefillTime: time.Now(),
        }
        tm.users[accountID] = user
        return user
    }

    func (u *User) refill() {
        now := time.Now()
        elapsed := now.Sub(u.lastRefillTime)

        // Calculate tokens to add based on elapsed time
        tokensToAdd := int64(elapsed.Seconds()) * u.refillRate
        if tokensToAdd > 0 {
            u.tokens = min(u.tokens+tokensToAdd, u.capacity)
            u.lastRefillTime = now
        }
    }

    func (u *User) AllowRequest() {
        u.mutex.Lock()
        defer u.mutex.Unlock()

        // Refill tokens based on time elapsed
        u.refill()

        // Check if we have at least one token
        if u.tokens > 0 {
            u.tokens--
            fmt.Printf("Request allowed. Tokens remaining: %d\n", u.tokens)
            return
        }

        // If no tokens available, panic
        panic("rate limit reached")
    }

    func min(a, b int64) int64 {
        if a < b {
            return a
        }
        return b
    }

    // Middleware handler function
    func (tm *TokenBucketManager) RateLimitMiddleware(accountID int64) {
        user := tm.GetOrCreateUser(accountID, 10, 1) // capacity=10, refillRate=1 token/sec
        user.AllowRequest()
    }

    func main() {
        tokenManager := NewTokenBucketManager()

        // Simulate requests with panic recovery
        for i := 0; i < 15; i++ {
            func() {
                defer func() {
                    if r := recover(); r != nil {
                        fmt.Printf("Request %d: %v\n", i+1, r)
                    }
                }()

                fmt.Printf("Request %d: ", i+1)
                tokenManager.RateLimitMiddleware(123)
            }()

            // Add some delay to see the refill in action
            if i == 9 { // After 10th request, wait to see refill
                fmt.Println("Waiting 2 seconds for token refill...")
                time.Sleep(2 * time.Second)
            } else {
                time.Sleep(100 * time.Millisecond)
            }
        }
    }
    ```
    </div>
    </details>

## Score
<h4><mark style="background-color:#ff9800; color:#ffffff; padding:4px 8px; border-radius:4px">6/10</mark></h4>

<p dir="rtl">
در کل خوب بود. استک php داشتن می‌خواستن سوییچ کنن رو go و تیم فلت بود، تعداد بکندها هم ۶ نفر و این یعنی فشار کاری! یه مقدار شاید اگه مسلط‌تر لایوکد رو می‌زدم اوکی می‌شد اما خب خیلی هم شرکتی نبود که براش ناراحت بشم.
</p>
