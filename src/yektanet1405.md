# [yektanet](https://yektanet.com)

### Status
#### 📜📞🔧❌
## Software Engineer
### Interview process
```mermaid
flowchart LR
    sr(Send resume) --> hr(HR call) --> ti1(1st Technical Interview) --rejected--x ti2("2nd Technical Interview") -.-> ti3("3rd Technical Interview") -.-> o(Offer)

```

### Apply way
Referral

### Interview Date
- **Sent Resume** <br /> 1405.05.10

- **HR Call**<br /> 1405.05.15

- **Technical Interview** <br> 1405.05.18 

- **Rejection Email** <br /> 1405.05.25

### Interview Duration
30 minutes

### Interview Platform
Google Meet


### Technical Interview (Live code)

<p dir="rtl">یه رشته رو بهش می‌گیم تراز در صورتی که تعداد کاراکترهای L و R توش برابر باشن. یه رشته‌ی تراز به عنوان ورودی به ما داده شده، اون رو به بیشتر تعداد زیررشته‌ی پیوسته‌ی تراز بشکن.</p>

**Examples:**
```
RLRRLLRLRL -> RL, RRLL, RL, RL
RLRRRLLRLL -> RL, RRRLLRLL
```

[LeetCode 1221 - Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/)

<details>
  <summary style="font-size:14px"><b><em>Answer</em></b></summary>
  <div>

  ```python
  def max_taraz(s: str):
      counter = 0
      result = []
      current_char = ""
      for ch in s:
          if ch == "R":
              counter += 1
              current_char += ch
          else:
              counter -= 1
              current_char += ch
          if counter == 0:
              result.append(current_char)
              current_char = ""

      return result

  # RLRRLLRLRL -> RL, RRLL, RL, RL
  # RLRRRLLRLL -> RL, RRRLLRLL
  s1 = "RLRRLLRLRL"
  s2 = "RLRRRLLRLL"
  s3 = ""
  a = max_taraz(s1)
  b = max_taraz(s2)
  c = max_taraz(s3)
  print(a, b, c)
  ```
  </div>
  </details>

### Score

<h4><mark style="background-color:#ff9800; color:#ffffff; padding:4px 8px; border-radius:4px">6/10</mark></h4>

<p dir="rtl">
نمیدونم چرا ریجکت کردن سوال رو هم درست زدم. بهتر، کی ضرر کرد؟ می‌خواستم برم رو Ad کار کنم همه ملت رو عاصی کنم، بعدیا بهترن همیشه. 😌😎
</p>
