# Topic: Module 1 - Python For Data Science, AI, and Development   

---

# 🔍 Regular Expressions (RegEx)

Regular Expressions (RegEx) are **patterns used to match, search, and manipulate text**.  
They are widely used in **data cleaning, parsing, and text validation**.

---

## 📌 Why Use RegEx?

    ✔ Efficient for finding and replacing patterns in text.
    ✔ Helps validate formats (emails, phone numbers, postal codes).
    ✔ Useful in text mining, data wrangling, and log analysis.
    ❌ Can be hard to read and maintain if patterns get too complex.
    ❌ Overuse can hurt performance on very large datasets.

---

## 🧩 Basic Elements

    .      → Any character except newline
    ^      → Start of string
    $      → End of string
    []     → Matches one character inside brackets
             Example: [aeiou] → matches vowels
    [^]    → Matches any character NOT inside brackets
             Example: [^0-9] → not a digit
    |      → OR
             Example: cat|dog → matches "cat" or "dog"
    ()     → Grouping
             Example: (ab)+ → "ab", "abab", "ababab"

---

## 🔢 Quantifiers

    *      → 0 or more times
    +      → 1 or more times
    ?      → 0 or 1 time
    {n}    → Exactly n times
    {n,}   → At least n times
    {n,m}  → Between n and m times

    Example:
        a{2,4} → matches "aa", "aaa", or "aaaa"

---

## 🔠 Character Classes

    \d     → Digit (0–9)
    \D     → Not a digit
    \w     → Word character (a–z, A–Z, 0–9, _)
    \W     → Not a word character
    \s     → Whitespace (space, tab, newline)
    \S     → Not whitespace

---

## 🎯 Anchors & Boundaries

    ^pattern   → Must start with "pattern"
    pattern$   → Must end with "pattern"
    \b         → Word boundary
                 Example: \bcat\b → matches "cat" but not "scatter"
    \B         → Not a word boundary

---

## ✅ Common Use Cases

    Email validation:
        ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

    Phone number (basic):
        ^\+?[0-9]{10,15}$

    Postal code (5 digits):
        ^\d{5}$

    Extract numbers:
        \d+

    Find all words:
        \w+

---

## 🐍 Python Examples

```python

import re

contact = r"Ronnel Belizar - 09154797401"
phone = r"\d\d\d\d\d\d\d\d\d\d\d"                 # Var for checking 11 digit number
match = re.search(phone, contact)                 # Checks "contact" if "phone" is found inside

if match:
    print("Phone number:", match.group())         # Retrieves the substring "09154797401"
else:
    print("Match not found")
    
---

• Always use raw strings (r"...") in Python to avoid escape issues.
• Test your patterns with https://regex101.com
• Keep patterns documented — regex can become unreadable quickly.

---

.      → Any character
^      → Start of string
$      → End of string
[]     → Any char in set
[^]    → Not in set
*      → 0 or more
+      → 1 or more
?      → 0 or 1
{n}    → Exactly n
{n,}   → At least n
{n,m}  → Between n and m
\d     → Digit
\w     → Word char
\s     → Whitespace
\b     → Word boundary
