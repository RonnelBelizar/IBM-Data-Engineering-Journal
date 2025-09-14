# Topic: Module 3 - Python Programming Fundamentals

# ⚡ Conditions & Branching (Data Engineering Context)

---

## 🔍 What It Is

    • Used to control program flow based on conditions (True / False).  
    • Essential for ETL pipelines, data validation, error handling.  
    • Makes decisions → run certain code only when criteria are met.  

---

## 🧾 Basic If Statement

    Example:
        value = 10
        if value > 5:
            print("Greater than 5")

---

## 🔀 If-Else

    Example:
        value = 3
        if value >= 5:
            print("Valid record")
        else:
            print("Invalid record")

---

## 🔗 If-Elif-Else

    Example:
        score = 85
        if score >= 90:
            print("Excellent")
        elif score >= 75:
            print("Good")
        else:
            print("Needs improvement")

---

## 🎭 Nested Conditions

    Example:
        user = "admin"
        access = True
        if user == "admin":
            if access:
                print("Access granted")
            else:
                print("Access denied")

---

## ⚖️ Logical Operators

    • and → both conditions must be True  
    • or  → at least one condition True  
    • not → inverts True/False  

    Example:
        age = 25
        has_id = True
        if age >= 18 and has_id:
            print("Allowed entry")

---

## 🛠️ Essential Functions / Patterns

    • Comparison:  ==, !=, <, <=, >, >=  
    • Membership:  in, not in  
    • Identity:    is, is not  

    Example:
        fruit = "apple"
        if fruit in ["apple", "banana", "orange"]:
            print("Valid fruit")

---

## ✨ Quick Recap

    • if → single condition check  
    • if-else → two-way branching  
    • if-elif-else → multi-way branching  
    • Nested if → decision trees  
    • Operators → and, or, not, in, is  

---

# 🔁 Loops (Data Engineering Context)

---

## 🔍 What It Is

    • Used to repeat actions until a condition is met.  
    • Essential for iterating over datasets, files, or API responses.  
    • Reduces repetitive code → makes ETL pipelines efficient.  

---

## 🔂 For Loop

    • Iterates over a sequence (list, tuple, dict, set, string).  

    Example:
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)

---

## 🔄 While Loop

    • Repeats until condition becomes False.  

    Example:
        count = 0
        while count < 5:
            print("Processing:", count)
            count += 1

---

## ⏭️ Break Statement

    • Stops the loop immediately.  

    Example:
        for num in range(10):
            if num == 5:
                break
            print(num)

---

## ↩️ Continue Statement

    • Skips current iteration, goes to next.  

    Example:
        for num in range(5):
            if num == 2:
                continue
            print(num)

---

## 🧮 Looping with Range

    • Common in data processing when you need index-based iteration.  

    Example:
        for i in range(3):
            print("Row:", i)

---

## 🧾 Looping Through Dictionaries

    Example:
        record = {"id": 101, "name": "Alice", "age": 30}
        for key, value in record.items():
            print(key, ":", value)

---

## 🛠️ Essential Functions / Patterns

    • range(start, stop, step) → number iteration  
    • enumerate(list)          → index + value  
    • zip(list1, list2)        → pair values  
    • dict.items()             → iterate key-value pairs  

    Example:
        ids = [1, 2, 3]
        names = ["Alice", "Bob", "Charlie"]
        for i, (id, name) in enumerate(zip(ids, names)):
            print(i, id, name)

---

## ✨ Quick Recap

    • for → iterate over a sequence  
    • while → repeat until condition false  
    • break → exit loop  
    • continue → skip to next iteration  
    • range, enumerate, zip → powerful looping helpers  

---

# 🛠️ Functions (Building Reusable Code)

---

## 🔍 What It Is

    • Functions are reusable blocks of code that perform a specific task.  
    • Helps avoid repetition → improves readability, maintainability, and debugging.  
    • In Data Engineering, functions are used for ETL steps, data cleaning, and transformations.  

---

## 🏗️ Defining a Function

    Syntax:
        def function_name(parameters):
            """docstring (optional: explains what it does)"""
            # code block
            return result

    Example:
        def greet(name):
            return f"Hello, {name}!"

        print(greet("Alice"))  # Output: Hello, Alice!

---

## 📥 Parameters & 📤 Return

    • Parameters → inputs the function accepts.  
    • Return → output the function sends back.  

    Example:
        def add_numbers(a, b):
            return a + b

        print(add_numbers(5, 7))  # Output: 12

---

## 🧰 Default Parameters

    • You can set default values for parameters.  

    Example:
        def connect_db(host="localhost", port=3306):
            return f"Connecting to DB at {host}:{port}"

        print(connect_db())  
        # Output: Connecting to DB at localhost:3306

---

## 🔀 Keyword & Positional Arguments

    Example:
        def full_name(first, last):
            return f"{first} {last}"

        print(full_name("Alice", "Smith"))  
        print(full_name(last="Smith", first="Alice"))

---

## 📦 *args & **kwargs

    • *args → variable-length positional arguments.  
    • **kwargs → variable-length keyword arguments.  

    Example:
        def log_event(*args, **kwargs):
            print("ARGS:", args)
            print("KWARGS:", kwargs)

        log_event("ERROR", "Disk full", user="admin", code=500)

---

## 📚 Docstrings (Documentation)

    • Triple quotes """...""" inside function → explains purpose.  

    Example:
        def square(n):
            """Returns the square of a number."""
            return n * n

        help(square)  # Displays docstring

---

## 🛠️ Essential Built-In Functions for DE

    • len() → length of object  
    • type() → type of variable  
    • str(), int(), float() → type conversion  
    • sum(), max(), min() → aggregations  
    • map(), filter(), lambda → quick transformations  
    • print() → debugging/logging  

---

## ✨ Quick Recap

    • Functions = reusable code blocks.  
    • Use parameters + return for flexibility.  
    • Default values, *args, **kwargs make them powerful.  
    • Essential for building ETL steps, transformations, and pipeline helpers.  


