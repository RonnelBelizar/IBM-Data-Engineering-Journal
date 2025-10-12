# Topic: Module 1 — Introducing Relational Database Products

---

# 🧠 Deep Dive into Advanced Relational Model Concepts

## 🔹 Functional Dependencies (FDs)
A **Functional Dependency (FD)** describes how one attribute determines another in a table.

**Definition:**  
If attribute A determines attribute B, it’s written as  
👉 `A → B` (read as “A functionally determines B”).

This means if two rows share the same value of A, they must have the same value of B.

**Example:**

| EmployeeID | Name  | Department |
|-------------|--------|------------|
| E01         | Maria | HR         |
| E02         | John  | IT         |
| E03         | Maria | HR         |

Here:  
✅ `EmployeeID → Name` and `EmployeeID → Department`  
❌ `Name → Department` (since “Maria” might appear in multiple departments)

**Scenario:**  
If you know a *student ID*, you can always find their *student name*.  
But knowing the *name* doesn’t always give you a unique *ID*.

---

### ⚙️ Properties of Functional Dependencies
1. **Reflexivity:** If B is a subset of A, then `A → B`.  
   Example: `{EmployeeID, Name} → Name`
2. **Augmentation:** If `A → B`, then `AC → BC`.  
   Example: `EmployeeID → Department` ⟹ `{EmployeeID, Location} → {Department, Location}`
3. **Transitivity:** If `A → B` and `B → C`, then `A → C`.  
   Example: `EmployeeID → Department` and `Department → Manager` ⟹ `EmployeeID → Manager`

---

## 🔹 Multivalued Dependencies (MVDs)
A **Multivalued Dependency (MVD)** exists when one attribute determines **multiple independent values** of another attribute.

**Definition:**  
If attribute A determines multiple values of B (independent of C), it’s written as 👉 `A ↠ B`.

**Example:**

| Student | Hobby     | Language |
|----------|------------|----------|
| Ana      | Painting  | English  |
| Ana      | Painting  | Spanish  |
| Ana      | Reading   | English  |
| Ana      | Reading   | Spanish  |

Here:  
✅ `Student ↠ Hobby` and `Student ↠ Language`  
because hobbies and languages are independent.

**Scenario:**  
A patient can have multiple *allergies* and multiple *prescriptions* — each list is unrelated.

---

### ⚙️ Properties of Multivalued Dependencies
1. **Complementation:** If `A ↠ B`, then `A ↠ (All attributes − A − B)`  
2. **Augmentation:** If `A ↠ B`, then `AC ↠ BC`  
3. **Transitivity:** If `A ↠ B` and `B ↠ C`, then `A ↠ C`

---

## 🔹 Candidate Keys
A **Candidate Key** is the *minimal set of attributes* that uniquely identify a row in a table.

**Example:**

| StudentID | Email           | Name |
|------------|----------------|------|
| 101        | ana@email.com  | Ana  |
| 102        | ben@email.com  | Ben  |

✅ Both `StudentID` and `Email` can uniquely identify each record → both are **Candidate Keys**.  
Only one becomes the **Primary Key**.

**Scenario:**  
In a hospital database, either:
- Patient ID, or  
- Combination of (Full Name + Date of Birth)  
can uniquely identify a patient.

---

## 🧩 Summary Table

| Concept                | Symbol | Description                            | Example                   |
|-------------------------|--------|----------------------------------------|----------------------------|
| Functional Dependency   | A → B  | A determines B                         | EmployeeID → Department    |
| Multivalued Dependency  | A ↠ B  | A determines multiple B values         | Student ↠ Hobby            |
| Candidate Key           | —      | Minimal unique identifier for a record | StudentID or Email         |

---

### 🧠 Quick Tip:
- **FDs** keep data *accurate*  
- **MVDs** keep data *organized*  
- **Candidate Keys** keep data *unique*  

Together, they make your database clean, efficient, and reliable 💪

