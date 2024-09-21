
# [wallex](https://wallex.ir/)

### Status
#### 📜📞🔧❌
## Senior Python developer
### Interview process
```mermaid
flowchart LR
    sr(Send resume) --> hr(HR call) --> ti(Technical Interview) --rejected--x hri(HR Interview) -.-> o(Offer)
```
### Apply Way
Site

### Interview Date

- **Sent Resume** <br /> 1403.06.03

- **HR Call**<br /> 1403.06.09

- **Technical Interview** <br> 1403.06.24 AT 11 AM

- **Rejection Email** <br /> 1403.06.27

### Interview Duration
- **Technical Interview** <br> 40 minutes

### Interview Platform
Google Meet

### Technical Interview

<p dir="rtl">
مصاحبه با خود CTO بود البته تو ایمیل گفته بودن که نفر دیگری هم هست ولی تو مصاحبه گفت نتونست بیاد و عذرخواهی کرد. بسیار آدم خفن و خوش‌برخورد و کولی بود. یه جوری بود که استرس نداشتی و خیلی صمیمی و دوستانه بود گفت‌وگو. سوالات هم غالبا از رزومه و تجربه کاری خودم بود. خبری از سوالات کنکوری و کانفیگی و الگوریتمی و این خزعبلات نبود بیشتر در مورد معماری و کانسپت سوال شد.
</p>

- Do you know wallex?

- Tell me about yourself.

- You said that you were responsible for developing the matching engine at the company. How do you scale a matching engine?

    We can use an engine per market or use concurrency algorithms like [L-Max](https://lmax-exchange.github.io/disruptor/disruptor.html).

- Writing and inserting data into the matching engine has become a bottleneck and slow for us. How can we solve this?

    We can avoid performing the write operation inside the matching engine and have it handle only the matching. We can send the matched orders to the database via a message broker and perform the write operation there (outside of the matching engine).

- Suppose we have a lot of requests and the number of our requests has increased. How do you handle this and manage it?

    Load balancing and an API gateway.

- We want to extract trading volumes based on daily, monthly, and yearly data. We have several rows that contain transactions, and our sum query is slow. How will you solve this problem?

    We have 3 tables for daily, monthly, and yearly data. At the end of each day, we can sum all trades and insert one integer into the daily table. Then, for the monthly total, we just have 30 integers to sum from the daily table, and for the yearly total, we have just 12 integers to sum for one year.

    After `SUM`ming daily volumes from **transactions** table (or sth like that), insert them into the **daily** table.
    ```
    daily
    +----+---------+---------------------+
    | ID | volume  | created_at          |
    +----+---------+---------------------+
    | 1  | 3450000 | 2024-09-21 16:54:41 |
    +----+---------+---------------------+
    ...
    +----+---------+---------------------+
    | 30 | 3450000 | 2024-09-21 16:54:41 |
    +----+---------+---------------------+
    ```

    Then we `SUM` the last 30 rows of the **daily** table and insert them into the **monthly** table.
    ```
    monthly
    +----+-----------+---------------------+
    | ID | volume    | created_at          |
    +----+-----------+---------------------+
    | 1  | 103500000 | 2024-09-21 16:54:41 |
    +----+-----------+---------------------+
    ...
    +----+-----------+---------------------+
    | 12 | 103500000 | 2024-09-21 16:54:41 |
    +----+-----------+---------------------+
    ```

    Then we `SUM` the last 12 rows of the **monthly** table and insert them into the **yearly** table.
    ```
    yearly
    +----+------------+---------------------+
    | ID | volume     | created_at          |
    +----+------------+---------------------+
    | 1  | 1242000000 | 2024-09-21 16:54:41 |
    +----+------------+---------------------+
    ```
    (volume amount is not important here)

- Math question: The market has reached a state where it has fallen 5 units, then after a while, it rises 1 unit, and this pattern has repeated. How can we predict the market for some time ahead (for example, a month)? How can we assess its probability? Do you have a solution?

    Analyze historical data. Calculate the frequency of these events in your dataset to estimate initial probabilities.
    And you can use calculate probabilities.

- You wrote in your resume that you worked with Kuber. How much do you know about it?

    Kubernetes is an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications.
    To the extent that I could bring it up, take it down, check to see what's down.

-  Did you write the Kuber files yourselves?

    No, the DevOps team wrote them. We only wrote the config maps.

- You said that you also played a role in designing the system. What did you do?

    I refactored several services here and completely rewrote some of them from scratch because we wanted to migrate from PHP to Go, and these went directly into production.

- Why do you want to leave (your current job) and why did you leave your previous place?

- What is important to you in work and the work environment?

    Culture and a friendly environment, respect, transparency and honesty, and having a plan.

- When you and your teammate have different ideas about how to tackle a problem, how do you work together to find a solution? What if they really push for their approach, even though you feel yours makes more sense?

    I try to convince them with reasons. If they are not convinced, I talk to the tech lead and let them make the decision, as the final word comes from the tech lead.

- Why is your tech lead the decision-maker?

    Because they have experience.

- Is it just experience?

    No, they also have responsibilities.

- What salary range do you have in mind?

- Any questions?

  I want to know about your teams, your company, your state, and things like these.

### Score
<h4><mark style="background-color:#54ca56">9/10</mark></h4>

<p dir="rtl">
به نظر خودم مصاحبه خوبی بود و امید خوبی به اکسپت شدن داشتم. حس می‌کنم اون سوال ریاضی و آماری رو خوب جواب ندادم ریجکت شد. در هر صورت خودم حس خوبی داشتم و خوب تونستم پرزنت کنم و با مایندست مصاحبه‌کننده هم خیلی حال کردم. بیشتر دنبال این بود که ببینه خب چی کارا کردی؟ این تجربه هایی که داشتی و اینا چجوری بوده؟ نگاهِ یه ربات استخدام کنم همه چی بلد باشه نداشت.
</p>
