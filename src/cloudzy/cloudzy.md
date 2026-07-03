# [Cloudzy | ابرناک](https://cloudzy.com/)

### Status
#### 📜📞🔧📝👱🏻‍♀️❌

## Back-End Developer

### Interview Process
```mermaid
flowchart LR
    sr(Send Resume) --> hr(HR Call) --> ti(Technical Interview) --> task(Task) --> hri(HR Interview) --rejected--x o(Offer)
```

### Apply Way
Jobinja

### Interview Date

- **Sent Resume**<br />Date not set

- **HR Call**<br />1404.02.24

- **Technical Interview**<br />1404.02.28

- **Rejection Email**<br />1404.03.13

### Interview Duration

- **Technical Interview**<br />30 minutes

- **Task Deadline**<br />3 days

- **HR Interview**<br /> 1 hour

### Interview Platform
Google Meet

### Technical Interview

- Tell me about yourself.

- Have you worked with Node.js?!

- What's your birth year?!

- If a git conflict occurs in our project, how can you determine whether it happens on the client-side or server-side? For example, during a `git pull` or `git push`, where do conflicts typically occur, and how would you handle them? Also, when you run git diff, does it operate on the client-side or server-side?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    Git conflicts always occur on the client-side during a merge. For example, if your local branch is behind the remote, a git pull may produce conflicts that you need to resolve locally. A git push can be rejected if the remote has new commits, but the actual conflict still happens when you merge locally. To resolve conflicts, you manually edit the conflicting files, stage them, and commit the merge.
    git diff is also a client-side operation—it shows differences in your local repository and does not access the server.
    </div>
    </details><br />

- What is hash table?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    In computer science, a hash table is a data structure that implements an associative array, also called a dictionary or simply map; an associative array is an abstract data type that maps keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. A map implemented by a hash table is called a hash map. 
    <a href="https://en.wikipedia.org/wiki/Hash_table#:~:text=In%20computer%20science,hash%20map" target="_blank" rel="noopener noreferrer">wikipedia</a><br />

    </div>
    </details><br />

- What is hash collision and how do you resolve it?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    https://www.youtube.com/watch?v=kNheXzNOcm4&t=251s

    </div>
    </details>

- What are the time complexities of search, insert, and delete in a linked list?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Search: O(n)
    Delete: O(1)
    Insert: O(1)
    https://www.bigocheatsheet.com/

    </div>
    </details>

- Are you familiar with Scrum?

- In Scrum, who is responsible for managing the process and addressing impediments when a task takes longer than expected (e.g., Product Owner, Scrum Master, or the development team)?

- What tools or frameworks do you use for unit testing in Go?

- You mentioned using BDD, how do you write BDD-style tests?

- What's difference between goroutine and thread?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    https://www.geeksforgeeks.org/go-language/golang-goroutine-vs-thread/

    </div>
    </details>

- What is the difference between pointer receivers and value receivers in Go?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    https://www.bogotobogo.com/GoLang/GoLang_Receiver_Value_vs_Pointer.php

    </div>
    </details>

- How do you detect memory leaks in Go?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">

    Using the `pprof` package to profile memory usage and inspect heap allocations.
    Observing increasing memory usage over time in long-running programs.
    Running Go’s race detector `(go run -race)` to catch goroutine leaks that may indirectly cause memory retention.
    https://dev.to/gkampitakis/memory-leaks-in-go-3pcn

    </div>
    </details>

- What can happen if goroutines are not properly stopped or cleaned up?
    <details>
    <summary style="font-size:14px"><b><em>Answer</em></b></summary>
    <div style="border:2px dashed #4a5568; padding:12px; border-radius:6px; margin-top:8px;  background-color: rgba(74,85,104,0.15);">
    If goroutines aren’t properly stopped, they can leak memory, waste CPU, and potentially cause deadlocks or resource exhaustion in the program.
    </div>
    </details>

- Any questions?

<p dir="rtl">
مصاحبه‌کننده در آخر فیدبک داد و گفت خوشم اومده ازت. (:
</p>

### Task

<p dir="rtl">
پس از مصاحبه فنی تسکی فرستادند که می‌تونید از
<a href="./cloudzytask.pdf">این‌جا</a>
ببینید. و همین‌طور 
<a href="https://github.com/mo1ein/cloudzy">جواب</a>
من رو.
</p>

### HR Interview
<p dir="rtl">
مصاحبه با دو نفر بود مدیرعامل و دستیارش! از این جلسه‌های گپ و گفت دوستانه! (متنفرم از این قسمت با این که راحت‌ترین قسمت هر مصاحبه‌ست برام). طی یه ساعت حرف زدن، حتی یه بار هم حرفی از حقوق و عدد و رقم نشد. سوال‌ها کاملاً اچ‌آری، کلیشه‌ای و قابل‌پیش‌بینی بود. از شرکت‌شون چیزای جالبی نشنیدم (می‌تونید سرچ کنید و بخونید) حتی اگه ردفلگ‌ها رو بذاریم کنار، چیزی نبود که بگم «وای چه جای خفنی!» ولی چیزی که واقعاً تو ذوقم زد رفتار مدیرعامل بود؛ یه وایب بالا به پایینی داشت، یه جوری که انگار خیلی تو دنیای تک و واقعیت تیم فنی نیست، پرت بود. همون‌جا تقریباً برام قطعی شد که دوست ندارم اونجا کار کنم. از اون به بعد سعی کردم خیلی نرم و مودب، ولی یه‌جوری رفتار کنم که اونا هم حال نکنن با من (: که اگه قراره رد بشه، از سمت اونا باشه نه من. از بیرون هم که نگاه می‌کردی، تیم‌شون پر از جونیور بود، حقوق کم، کار زیاد، همون ترکیب کلاسیک «بیای رشد کنی ولی بسوزی».
</p>

### Score
<h4><mark style="background-color:#DC3545"; color:#ffffff; padding:4px 8px; border-radius:4px">4/10</mark></h4>
