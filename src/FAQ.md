<h2 align="center" id="rejection" dir="rtl"><a class="header" href="#rejection">سوالات پرتکرار  |  FAQ</a></h2>

<p dir="rtl">
این‌جا سوالات پرتکراری که تو مصاحبه می‌پرسن رو به همراه جواب، یک‌جا جمع کردم.
</p>


<img src="assets/bullshit_everywhere_meme.jpg" alt="bullshit_everywhere_meme" style="display: block; max-width: 60%; width: 100%; height: auto; margin-left: auto; margin-right: auto; border-radius: 5px; margin-top: 5px;">



### Go

**_Is go an OOP language?_** <br />
**_(3 times - [ozone](mo1ein.github.io/jobname/ozone.html#:~:text=Is%20Golang%20an%20OOP%20language%3F), [hamkaran-system](https://mo1ein.github.io/jobname/hamkaran-system.html?highlight=hamkaran#status:~:text=What%20is%20OOP%20concepts%20that%20go%20don%27t%20have%20it%3F), [sternx](https://mo1ein.github.io/jobname/sternx/sternx.html?highlight=sternx#sternx:~:text=Go%20doesn%27t%20have%20classes%20and%20is%20not%20based%20on%20OOP%20principles.%20Can%20you%20explain%20that%3F))_**
- [go.dev](https://go.dev/doc/faq#:~:text=Yes%20and%20no,to%20structs%20(classes).)

**_Go has inheritance concept?_**

No. Inheritance means inheriting the properties of the superclass into the base class and is one of the most important concepts in Object-Oriented Programming. Since Golang does not support classes, so inheritance takes place through struct embedding. We cannot directly extend structs but rather use a concept called composition where the struct is used to form other objects. So, you can say there is No Inheritance Concept in Golang.

**_What is Mutex?_**

**_What is goroutine?_**

**_What is channel?_**

**_What is waitgroup?_**

**_How go manage memory? how garbage collector work?_**

### Python
**_What is decorator?_** <br />
**_(5 times - [digikala](https://mo1ein.github.io/jobname/digikala/digikala.html?highlight=decorator#technical-interview:~:text=What%20is%20RPC%3F-,What%20is%20decorator%3F,-What%20feature%20of), [siz-tel](https://mo1ein.github.io/jobname/siztel/internship.html?highlight=What%20is%20python%20decorator?#technical-interview), [exalab](https://mo1ein.github.io/jobname/exalab.html#:~:text=What%20is%20decorator%3F%20and%20where%20do%20you%20use%20it%3F%20do%20you%20write%20decorator%3F), [karnameh](), [sternx]())_**
- [geeksforgeeks (short description)](https://www.geeksforgeeks.org/decorators-in-python/)
- [realpython](https://realpython.com/primer-on-python-decorators/)

**_Why are we able to change python tuple values even though they are immutable? Suppose:_** <br />
**_(1 times - [snapp](https://mo1ein.github.io/jobname/snapp/snapp_cab_2.html?highlight=tuple#1st-technical-interview:~:text=Why%20are%20we%20able%20to%20change%20python%20tuple%20values%20even%20though%20they%20are%20immutable%3F))_**
```python
a = 1
b = 2
a, b = b, a
```

Tuple Packing: When you write `a, b = 1, 2` Python is packing the values 1 and 2 into a `tuple (1, 2)`, and then unpacking them into the variables a and b. This is a convenient way to assign multiple variables at once.

```python
a, b = 1, 2
# This is equivalent to:
# temp_tuple = (1, 2)
# a = temp_tuple[0]
# b = temp_tuple[1]
```

Tuple Unpacking: When you write `a, b = b, a` Python is creating a `tuple (b, a)` with the current values of b and a, and then unpacking this tuple back into the variables a and b. This is a common idiom in Python for swapping the values of two variables without needing a temporary variable.
```python
a, b = b, a
# This is equivalent to:
# temp_tuple = (b, a)
# a = temp_tuple[0]
# b = temp_tuple[1]
```

Why This Works
Immutability of Tuples: The immutability of tuples means that the tuple itself cannot be changed after it is created. However, this doesn't prevent you from creating new tuples or reassigning variables to new tuples.
Variable Reassignment: The operation `a, b = b, a` involves creating a new tuple and then reassigning the variables a and b to the elements of this new tuple. The original tuple `(a, b)` is not modified; instead, new tuples are created and the variables are updated to reference these new tuples.

**_Python is call by reference or call by value?_** <br />
**_(1 times - [narvan](https://mo1ein.github.io/jobname/narvan.html#interview-date:~:text=Python%20is%20call%20by%20reference%20or%20call%20by%20value%3F))_**

In Python, the concepts of "call by value" and "call by reference" are often discussed, but Python actually uses a mechanism sometimes referred to as "call by object reference" or "call by assignment" . Here's what this means:
Call by Object Reference
Immutable Objects: When you pass immutable objects (like integers, strings, or tuples) to a function, Python behaves similarly to "call by value." This means that the function receives a copy of the reference to the object, and since the object itself cannot be changed, any modifications within the function do not affect the original object outside the function. For example, if you pass a string to a function and attempt to change it, the original string remains unchanged .
Mutable Objects: When you pass mutable objects (like lists, dictionaries, or sets) to a function, Python allows changes made within the function to affect the original object outside the function. This is because the function receives a reference to the object, and since the object is mutable, modifications are reflected in the original object. This behavior is often likened to "call by reference"

**_How does python manage memory? Explain python memory management._**

- [realpython](https://realpython.com/python-memory-management/)

**_What is the difference between concurrency in python and go?_**
todo

### Database

**_SQL vs NoSQL._** <br />
**_(4 times - [snapp](https://mo1ein.github.io/jobname/snapp/snapp_cab_2.html#1st-technical-interview:~:text=semantic%20versioning%20is%3F-,SQL%20vs%20NoSQL,-What%20is%20CAP), [exalab](https://mo1ein.github.io/jobname/exalab.html#:~:text=What%20is%20the%20difference%20between%20SQL%20and%20NoSQL%3F), [siz-tel](https://mo1ein.github.io/jobname/siztel/junior.html#technical-interview:~:text=Difference%20between%20SQL%20and%20NoSQL%20databases%3F%20Which%20one%20is%20faster%3F), [narvan](https://mo1ein.github.io/jobname/narvan.html#technical-interview:~:text=you%20worked%20with%3F-,What%20is%20NoSql%3F,-mongoDB%20is%20a))_**

- [datacamp](https://www.datacamp.com/blog/sql-vs-nosql-databases#:~:text=hashes%2C%20and%20sets.-,Key%20Differences%20Between%20SQL%20and%20NoSQL,-Let%E2%80%99s%20compare%20SQL)
- [geeksforgeeks](https://www.geeksforgeeks.org/difference-between-sql-and-nosql/)

**_What is ACID?_** <br />
**_(3 times - [digikala](https://mo1ein.github.io/jobname/digikala/digikala.html#technical-interview:~:text=for%20DevOps%20stuffs%3F-,What%20is%20ACID%3F,-Can%20you%20example), [karnameh](https://mo1ein.github.io/jobname/karnameh.html#technical-interview:~:text=in%20a%20database%3F-,What%20is%20ACID%3F,-Any%20questions%3F), [mhholding](https://mo1ein.github.io/jobname/mhholding.html#1st-technical-interview:~:text=image%20in%20docker%3F-,What%20is%20ACID%3F,-What%20is%20nginx))_**

- [wikipedia](https://en.wikipedia.org/wiki/ACID)

**_Why redis is fast?_**

**_Say some redis data structures._**

**_What is indexing? How database index columns?_** <br />
**_(3 times - [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=What%20is%20index%20in%20database%3F), [snapp](https://mo1ein.github.io/jobname/snapp/snapp_cab_2.html#1st-technical-interview:~:text=What%20is%20index,indexing%20is%20bad%3F), [karnameh](https://mo1ein.github.io/jobname/karnameh.html#technical-interview:~:text=What%20is%20indexing%3F%20and%20why%20is%20bad%20when%20use%20a%20lot%3F), [quiz of kings](https://mo1ein.github.io/jobname/QuizOfKings.html#technical-interview:~:text=How%20do%20database%20index%20columns%20work%3F))_**

- [atlassian](https://www.atlassian.com/data/databases/how-does-indexing-work)

**_Why use indexing a lot, is a bad thing?_** <br />
**_(3 times - [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=Why%20shouldn%27t%20we%20index%20all%20columns%3F%20Doesn%27t%20it%20become%20faster%3F), [snapp](https://mo1ein.github.io/jobname/snapp/snapp_cab_2.html#1st-technical-interview:~:text=What%20is%20index,indexing%20is%20bad%3F), [karnameh](https://mo1ein.github.io/jobname/karnameh.html#technical-interview:~:text=What%20is%20indexing%3F%20and%20why%20is%20bad%20when%20use%20a%20lot%3F))_**

1. Increased Storage Requirements <br />
While having more space might seem beneficial, each index consumes additional disk space. For large databases, this can lead to significant storage overhead, especially if many indexes are created on various columns that may not be frequently queried.

2. Slower Write Operations <br />
Every time a record is inserted, updated, or deleted, all associated indexes must also be updated. This can slow down write operations considerably. For databases with high transaction volumes, the overhead of maintaining numerous indexes can lead to performance bottlenecks.

3. Index Maintenance Overhead <br />
Indexes require regular maintenance to ensure they remain efficient. Over time, as data is modified, indexes can become fragmented, which can degrade performance. This maintenance can be resource-intensive, requiring additional processing time and effort.

4. Diminished Query Performance <br />
While indexes are designed to speed up read operations, having too many can lead to confusion for the query optimizer. The optimizer may struggle to determine which index to use for a given query, potentially leading to suboptimal execution plans and slower performance.

5. Complexity in Query Optimization <br />
With many indexes, the complexity of the query optimization process increases. The database management system (DBMS) must evaluate multiple indexes to determine the most efficient way to execute a query. This can lead to longer planning times and may not always result in the best performance.

6. Reduced Performance for Certain Queries <br />
Some queries may not benefit from additional indexes, particularly those that involve complex joins or aggregations. In such cases, the overhead of maintaining multiple indexes can outweigh the performance benefits, leading to slower overall query execution.

**_What are database isolation levels?_**

- [geeksforgeeks](https://www.geeksforgeeks.org/transaction-isolation-levels-dbms/)
- [wikipedia](https://en.wikipedia.org/wiki/Isolation_(database_systems))

**_We have a query that is too slow, how you try to fast it?_** <br />
**_(2 times, [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=We%20have%20a%20query%20that%20is%20too%20slow%2C%20how%20you%20try%20to%20fast%20it%3F), [hamkaran system](https://mo1ein.github.io/jobname/hamkaran-system.html#live-code:~:text=If%20our%20query%20is%20slow%2C%20how%20would%20you%20optimize%20it%3F%20What%20is%20your%20solution%20for%20this%20problem%3F))_**

1. Analyze the Query Execution Plan <br />
Use `EXPLAIN`: Run the query with the `EXPLAIN` command (or `EXPLAIN ANALYZE` for more detailed output) to understand how the database engine executes the query. This will provide insights into which indexes are being used, join methods, and where potential bottlenecks lie.
Identify Slow Operations: Look for operations that have high costs, such as full table scans, large sorts, or expensive joins.

2. Optimize Index Usage<br />
Create Indexes: Ensure that appropriate indexes are in place for columns used in `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` clauses.
Review Existing Indexes: Check if existing indexes are being utilized effectively. Sometimes, redundant or unused indexes can slow down write operations.
Consider Composite Indexes: If multiple columns are frequently queried together, consider creating composite indexes.

3. Rewrite the Query<br />
Simplify the Query: Break down complex queries into simpler sub-queries or Common Table Expressions (CTEs) to improve readability and performance.
*Avoid SELECT : Instead of selecting all columns, specify only the columns you need. This reduces the amount of data processed and transferred.
Use EXISTS Instead of IN: If applicable, using `EXISTS` can be faster than `IN` for subqueries, especially when dealing with large datasets.

4. Optimize Joins<br />
Check Join Conditions: Ensure that join conditions are using indexed columns.
Limit the Number of Joins: If possible, reduce the number of joins or rearrange them to optimize performance.
Use `INNER JOIN` Instead of `OUTER JOIN`: If you don’t need all rows from both tables, prefer `INNER JOIN` as it can be more efficient.

5. Use Query Caching<br />
Enable Query Caching: If your database supports it, enable query caching for frequently executed queries. This can significantly reduce execution time for repeated queries.

6. Partition Large Tables<br />
Table Partitioning: For very large tables, consider partitioning them based on certain criteria (e.g., date ranges). This can improve query performance by limiting the amount of data scanned.

7. Optimize Database Configuration<br />
Tune Database Settings: Review and optimize database configuration settings such as memory allocation, cache sizes, and connection limits based on your workload.

8. Monitor and Analyze Performance<br />
Use Monitoring Tools: Employ database monitoring tools to track query performance over time and identify trends or recurring issues.
Log Slow Queries: Enable slow query logging to capture queries that exceed a certain execution time, allowing you to focus on optimizing the most problematic queries.

9. Consider Denormalization<br />
Denormalization: In some cases, denormalizing the database schema (i.e., combining tables) can improve performance for read-heavy applications, at the cost of increased complexity for write operations.

10. Review Application Logic<br />
Optimize Application Code: Sometimes, the issue may not be with the query itself but with how it is called from the application. Review the application logic to ensure that it is making efficient use of database queries.

### Git
**_Merge vs Rebase... explain differneces and pros and cons._** <br />
**_(3 times - [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=What%20is%20difference%20between%20git%20Merge%20and%20Rebase%3F), [wallex](https://mo1ein.github.io/jobname/wallex1402.html#wallex:~:text=Why%20did%20you%20not%20choose%20to%20rebase%20instead), [sternx](https://mo1ein.github.io/jobname/sternx/sternx.html#1st-technical-interview:~:text=know%20about%20git%3F-,What%20is%20git%20rebase%3F,-What%27s%20your%20salary))_**
- [coderefinery](https://coderefinery.github.io/git-branch-design/01-rebase/)
- [codeparrot](https://codeparrot.ai/blogs/git-merge-vs-rebase)
- [geeksforgeeks](https://www.geeksforgeeks.org/git-difference-between-merging-and-rebasing/)

**_What was your git flow at your previous company?_** <br />
**_(3 times - [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=What%20was%20your%20git%20flow%20at%20your%20previous%20company%3F), [wallex](https://mo1ein.github.io/jobname/wallex1402.html?highlight=walle#wallex:~:text=What%20was%20your%20git%20flow%20at%20your%20previous%20company%3F), [digikala](https://mo1ein.github.io/jobname/digikala/digikala.html#:~:text=What%20was%20your%20Git%20workflow%20in%20the%20last%20company%3F))_**

**_What is fast-forward?_** <br />
**_(1 times - [snappshop](https://mo1ein.github.io/jobname/snapp/snappshop.html#:~:text=What%20is%20fast%2Dforward%3F))_**
- [graphite](https://graphite.dev/guides/git-fast-forward-merge)
- [atlassian](https://www.atlassian.com/git/tutorials/using-branches/git-merge#:~:text=A%20fast%2Dforward%20merge%20can,look%20something%20like%20the%20following%3A)

### Design Pattern

**_What is SOLID?_** <br />
**_(4 times - [snapp](https://mo1ein.github.io/jobname/snapp/snapp_cab_2.html#:~:text=What%20is%20SOLID%3F%20tell%20us%20about%202%20of%20them.), [wallex](https://mo1ein.github.io/jobname/wallex1402.html#:~:text=is%20it%20good%3F-,What%20is%20SOLID%3F,-What%20is%20dependency), [digikala](https://mo1ein.github.io/jobname/digikala/digikala.html#:~:text=us%20about%20yourself.-,What%20is%20SOLID%3F,-What%20is%20DI), [itoll](https://mo1ein.github.io/jobname/itoll.html#:~:text=is%20design%20pattern%3F-,What%20is%20SOLID%3F,-Difference%20between%20list))_**
- [wikipedia](https://en.wikipedia.org/wiki/SOLID)
