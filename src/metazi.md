# [Metazi](https://metazigroup.com)

### Status
#### 📜📞🔧❌

## Back-End Developer

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> ti(Technical Interview) --rejected--x hri(HR Interview) -.-> o(Offer)
```

### Apply Way
Jobvision

### Interview Date
- **Sent Resume**<br />1404/07/01

- **HR Call**<br />1404/07/06

- **Technical Interview**<br />1404/07/07

- **Rejection Email**<br />1404/07/08

### Interview Duration
- **Technical Interview**<br />45 minutes

### Interview Platform
Google Meet

### Technical Interview
- Tell me about yourself.

- What is `init` in Go? How does it work and how does it differ from `main`?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    [go.dev](https://go.dev/doc/effective_go#init)

    `init()` is a special function: `func init()`. It runs automatically after package-level variables are initialized. You can have multiple `init()`s in a package. You cannot call `init()` yourself.

    Order: evaluate package vars → run that package’s `init()`s → repeat by dependency order → finally call `main.main()`.

    `main()` is the program entry point (`package main`, `func main()`) and runs once after all `init()`s finish.

    </div>
    </details>

- What is `_` in imported packages?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    `_` is the blank identifier. When used in an import like `import _ "pkg/path"` it means: import the package solely for its side effects (package initialization) but do not bind any name to refer to it in the importing file. The compiler won’t complain about an unused import because the blank identifier intentionally discards the package name.

    ```go
    import (
        _ "github.com/lib/pq" // register pq as a database/sql driver via its init()
    )
    ```

    (Aside: `_` is also used to discard values in assignments: `_, ok := m["x"]`.)

    </div>
    </details>

- Why use it? If there is no need, should we remove it? Why do people still use it?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Use them when the package’s `init()` performs necessary side effects (driver registration, plugin/handler registration, global initialization). If a package has no needed side effects, remove the import.

    </div>
    </details>

- Why write configs in `init` instead of `main`? What are the benefits? What are the problems if we write all code in `init` instead of `main`?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Pros: `init()` runs before `main()`, so it can prepare package-level state.

    Cons: `init()` cannot accept `context` or return errors, runs during tests, runs before flag/config parsing, and makes shutdown/signal handling hard. Prefer `main()` for orchestration, lifecycle and graceful shutdown.

    </div>
    </details>

- Multiple packages each run an `init` that `Printf`s the package name. You import them in `main`, but `main()` is empty. What is the output?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    ```go
    // pkg/a/a.go
    package a

    import "fmt"

    func init() { fmt.Println("init a") }

    // pkg/b/b.go
    package b

    import "fmt"

    func init() { fmt.Println("init b") }

    // main.go
    package main

    import (
        _ "example.com/project/pkg/a"
        _ "example.com/project/pkg/b"
    )

    func main() {} // empty
    ```

    Important notes about the order:

    - Initialization (and therefore the `init()` prints) runs before `main()` is called.
    - The order between packages follows the import dependency graph: if `b` imports `a`, `init a` will always appear before `init b`.
    - If the packages are independent (neither imports the other), the relative order is unspecified — you should not rely on a particular ordering.
    - `main()` being empty produces no additional output.

    </div>
    </details>

- If you have multiple goroutines that fetch data from different APIs and you want to gather all results and aggregate them, or wait with a timeout then aggregate, how can you do this?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    ```go
    package main

    import (
        "fmt"
        "sync"
        "time"
    )

    type Result struct {
        URL  string
        Body string
        Err  error
    }

    func fetch(url string) (string, error) {
        // do actual HTTP call...
        return "data-for-" + url, nil
    }

    func fetchPartial(urls []string, timeout time.Duration) map[string]string {
        var wg sync.WaitGroup
        resultsCh := make(chan Result, len(urls))

        for _, u := range urls {
            wg.Add(1)
            go func(u string) {
                defer wg.Done()
                body, err := fetch(u)
                resultsCh <- Result{URL: u, Body: body, Err: err}
            }(u)
        }

        // close channel when all goroutines are done
        go func() {
            wg.Wait()
            close(resultsCh)
        }()

        aggregated := make(map[string]string)
        timeoutCh := time.After(timeout)

    Loop:
        for {
            select {
            case r, ok := <-resultsCh:
                if !ok {
                    break Loop // channel closed, all responses received
                }
                if r.Err == nil {
                    aggregated[r.URL] = r.Body
                } else {
                    // optionally log r.Err
                }
            case <-timeoutCh:
                // timeout occurred — stop waiting for more, but goroutines may still be running.
                // To avoid leaks in real code, pass a context to requests so they cancel.
                break Loop
            }
        }
        return aggregated
    }

    func main() {
        urls := []string{"a", "b", "c"}
        out := fetchPartial(urls, 2*time.Second)
        fmt.Println(out)
    }
    ```

    </div>
    </details>

- If you run `main.go`, how many goroutines are initialized?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    At least one main goroutine plus several runtime goroutines (GC, timers, netpoller). You commonly see 2–4 at startup, but exact number varies. `GOMAXPROCS` controls parallelism (Ps), not total goroutine count.

    </div>
    </details>

- How does Go manage goroutines?

    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    The runtime scheduler uses three core concepts: G, M, and P.

    - G (goroutine): the user-level unit of concurrency (stack, state, metadata). Goroutines are cheap to create and their stacks grow and shrink as needed.
    - M (machine): an OS thread that actually executes Go code. The runtime creates and reclaims Ms as needed (e.g., to service blocking syscalls).
    - P (processor): a scheduler context that holds a run queue of runnable Gs and scheduling state. Only an M that has an associated P can run Go code. `GOMAXPROCS` controls how many Ps exist (how many goroutines can run in parallel).

    How scheduling works (high level):

    - Each P has a local run queue of runnable goroutines. When a goroutine becomes runnable it’s pushed to a P’s queue. When a P runs out of work it will steal goroutines from other Ps or pull from a global queue; this provides locality and load balancing.
    - The scheduler chooses a G from a P’s run queue and runs it on the M bound to that P. If that G blocks (channel wait, sleep, blocking syscall), it is parked and another G is scheduled.

    </div>
    </details>


### Score
<h4><mark style="background-color:#54ca56">6/10</mark></h4>
