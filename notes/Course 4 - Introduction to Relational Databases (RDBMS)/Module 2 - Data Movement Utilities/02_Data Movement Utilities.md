# Topic: Module 2 — Creating Tables and Loading Data

---

# 🗃️ Database Objects and Hierarchy

## Database Hierarchy

- **Instance** – The running database environment that manages memory, processes, and data files.  
  *Example:* PostgreSQL instance running on port 5432.

- **RDBMS (Relational Database Management System)** – Software that manages relational data using SQL.  
  *Example:* MySQL, PostgreSQL, Oracle.

- **Schemas** – Logical containers that organize database objects.  
  - **Internal Schema:** Defines physical storage (e.g., indexing, data files).  
  - **External Schema:** Defines user views and permissions.  
  *Example:* `public` schema or `sales` schema.

- **Database Partition** – Divides large tables or indexes into smaller, more manageable pieces for better performance.  
  *Example:* Partition a `transactions` table by `year` → 2023, 2024, 2025.

---

## Database Objects

- **Tables** – Store data in rows and columns.  
  ```sql
  CREATE TABLE employees (
      emp_id SERIAL PRIMARY KEY,
      name VARCHAR(100),
      department VARCHAR(50)
  );


- **Constraints** – Enforce data integrity rules.  
*Types:* PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL.  

```sql
ALTER TABLE employees
ADD CONSTRAINT chk_dept CHECK (department <> '');
```

- **Views** – Virtual tables created from queries.  

```sql
CREATE VIEW active_employees AS
SELECT name, department
FROM employees
WHERE department IS NOT NULL;
```

- **Aliases** – Temporary names for tables or columns to simplify queries.  

```sql
SELECT e.name AS employee_name
FROM employees e;
```

---

## 🧩 Summary

| Concept     | Description                | Example                     |
|--------------|----------------------------|------------------------------|
| Instance     | Running DB environment     | PostgreSQL on port 5432      |
| RDBMS        | Software managing databases | MySQL, Oracle                |
| Schema       | Logical grouping of objects | `public`, `sales`            |
| Partition    | Splitting large data sets   | `transactions_2025`          |
| Table        | Data storage structure      | `employees`                  |
| Constraint   | Data integrity rule         | `PRIMARY KEY`, `CHECK`       |
| Index        | Query performance booster   | `CREATE INDEX`               |
| View         | Virtual table from query    | `CREATE VIEW`                |
| Alias        | Temporary name in query     | `SELECT e.name`              |

---

# 🔑 Primary Keys and Foreign Keys

## Primary Key

A **Primary Key** uniquely identifies each record in a table.  
It ensures that no two rows have the same key value and that the key column(s) cannot contain NULL.

**Key Points:**
- Every table should have one primary key.
- A primary key can be a single column or a combination of columns (composite key).
- Automatically creates a unique index.

**Example 1: Single-column primary key**

```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);
```

**Example 2: Composite primary key**

```sql
CREATE TABLE project_assignments (
    emp_id INT,
    project_id INT,
    PRIMARY KEY (emp_id, project_id)
);
```

---

## Foreign Key

A **Foreign Key** is a field (or combination of fields) that creates a relationship between two tables.  
It references the **Primary Key** of another table, maintaining **referential integrity**.

**Key Points:**
- Links data across tables.
- Prevents invalid data entry (e.g., referencing a non-existing record).
- Can cascade updates or deletions.

**Example 1: Basic foreign key relationship**

```sql
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
```

---

## 🧩 Summary

| Concept              | Description                                                | Example / Keyword                         |
|-----------------------|------------------------------------------------------------|--------------------------------------------|
| Primary Key           | Uniquely identifies each row in a table                    | `PRIMARY KEY (emp_id)`                     |
| Foreign Key           | References a primary key in another table                  | `FOREIGN KEY (dept_id) REFERENCES ...`     |
| Composite Key         | Combines two or more columns to uniquely identify a record | `PRIMARY KEY (emp_id, project_id)`         |
| Referential Integrity | Ensures consistency between related tables                 | Prevents invalid foreign key references    |
| Cascade               | Automatically updates or deletes dependent rows            | `ON DELETE CASCADE`, `ON UPDATE CASCADE`   |

---

# 🧭 Overview of Indexes in Databases

Indexes are special data structures that make **data retrieval faster** — like a book’s index that helps you find topics quickly without reading every page. 📖✨  
When you run a SELECT query, the database can use an **index** to find rows efficiently instead of scanning the whole table. 🚀  

---

💡 **What Is an Index?**  
An index is created on one or more columns to speed up searching and sorting operations.  

👉 Example:
```sql
CREATE INDEX idx_employee_name ON employees (name); 
```

```sql 
SELECT * FROM employees WHERE name = 'Alice';  
```

✅ Faster because it jumps straight to the record instead of scanning all rows.

---

⚡ **Benefits**  
- Speeds up queries with WHERE, JOIN, or ORDER BY  
- Improves performance on large datasets  

🐢 **Drawbacks**  
- Slower INSERT, UPDATE, DELETE (since indexes must also update)  
- Takes extra storage space 💾  

---

🔹 **Common Types of Indexes**  

**Primary Index** – Created automatically on a table’s primary key.  
Example: 
```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY, 
    name VARCHAR(50)
    ); 🔑  
```

**Composite Index** – Combines multiple columns for complex searches.  
Example: 
```sql
CREATE INDEX idx_dept_name ON employees (department, name); 🧠  
```

**Full-text Index** – Speeds up text searches.  
Example: 
```sql
CREATE INDEX idx_article_content ON articles USING gin(to_tsvector('english', content)); 🔍  
```

# 🧩 Example: Table with an Index

Let’s say you have an `employees` table like this 👇

| emp_id | name      | department | email                |
|--------:|-----------|-------------|-----------------------|
| 1       | Alice     | HR          | alice@company.com     |
| 2       | Bob       | IT          | bob@company.com       |
| 3       | Charlie   | Finance     | charlie@company.com   |
| 4       | Diana     | IT          | diana@company.com     |
| 5       | Edward    | HR          | edward@company.com    |

---

## 🧱 Create an Index
If we create an index on the `name` column:

`CREATE INDEX idx_employee_name ON employees (name);`

Nothing changes **visually** in the table — it still looks the same.  
But behind the scenes, the database builds a **sorted structure** (like a mini phonebook 📒) for the `name` column.

---

## ⚙️ How It Helps
When you search:

`SELECT * FROM employees WHERE name = 'Charlie';`

👉 The database doesn’t check every row.  
Instead, it goes straight to the “C” section of its internal index — making the search super fast! ⚡  

Without the index, it would scan all 5 rows one by one (called a **full table scan**). 🐢

---

🧠 **Remember:**  
- Indexes improve search speed 🚀  
- But every `INSERT`, `UPDATE`, or `DELETE` also updates the index — so use them wisely 💾

---

🧠 **Quick Tip:**  
Use indexes **strategically** — only on columns often used in filters or joins.  
Too many indexes = slower writes and wasted space! ⚙️

---

# 🧩 Database Normalization

**Normalization** is the process of organizing data in a database to **reduce redundancy** (repeated data) and **improve integrity**.  
It splits large tables into smaller ones that are logically connected — making the database more efficient and easier to maintain. 🧠✨  

---

## 🥇 First Normal Form (1NF)
✅ Each row is **unique** (has a unique identifier).  
✅ Each cell has a **single value** — no repeating groups or lists.  

**Before (Not in 1NF):**

| student_id | name   | subjects            |
|-------------|--------|--------------------|
| 1           | Alice  | Math, English      |
| 2           | Bob    | Science, English   |

❌ Multiple subjects in one cell = not 1NF.

**After (In 1NF):**

| student_id | name   | subject  |
|-------------|--------|----------|
| 1           | Alice  | Math     |
| 1           | Alice  | English  |
| 2           | Bob    | Science  |
| 2           | Bob    | English  |

✅ Each cell has one value only.  
✅ Each row is unique.

---

## 🥈 Second Normal Form (2NF)
✅ Must already be in **1NF**.  
✅ Move data that applies to multiple rows into a **separate table** to remove *partial dependencies*.  

**Before (Not in 2NF):**

| student_id | course_id | student_name | course_name |
|-------------|------------|---------------|--------------|
| 1           | C1         | Alice         | Math         |
| 2           | C2         | Bob           | English      |
| 1           | C2         | Alice         | English      |

❌ `student_name` depends only on `student_id`, not the whole key.

**After (In 2NF):**

**students**

| student_id | student_name |
|-------------|---------------|
| 1           | Alice         |
| 2           | Bob           |

**courses**

| course_id | course_name |
|------------|-------------|
| C1         | Math        |
| C2         | English     |

**enrollments**

| student_id | course_id |
|-------------|------------|
| 1           | C1         |
| 1           | C2         |
| 2           | C2         |

✅ Each table focuses on one type of data.  

---

## 🥉 Third Normal Form (3NF)
✅ Must already satisfy **1NF** and **2NF**.  
✅ Remove *transitive dependencies* (when one non-key depends on another non-key).  

**Before (Not in 3NF):**

| student_id | name   | department | dept_head   |
|-------------|--------|-------------|--------------|
| 1           | Alice  | IT          | Mr. Smith    |
| 2           | Bob    | HR          | Ms. Perez    |

❌ `dept_head` depends on `department`, not directly on `student_id`.

**After (In 3NF):**

**students**

| student_id | name   | department |
|-------------|--------|-------------|
| 1           | Alice  | IT          |
| 2           | Bob    | HR          |

**departments**

| department | dept_head |
|-------------|------------|
| IT          | Mr. Smith  |
| HR          | Ms. Perez  |

✅ Now every column depends **only** on the primary key.

---

## ⚙️ Normalization in OLTP vs OLAP

**OLTP (Online Transaction Processing)** 🏦  
- Used for real-time systems (like hospital or banking systems).  
- Databases are **highly normalized** (up to 3NF or more).  
- Goal: Avoid redundancy, ensure consistency, fast updates.

**OLAP (Online Analytical Processing)** 📊  
- Used for analytics and reporting (like dashboards, BI tools).  
- Databases are **denormalized** for performance.  
- Goal: Speed up read operations and aggregations.

---

🧠 **Quick Tip:**  
- **Normalize** → better for fast, accurate transactions.  
- **Denormalize** → better for quick reporting and data analysis. 🚀

---

# 🧱 Relational Model Constraints

In a **Relational Database**, **constraints** are rules that ensure the **accuracy, consistency, and validity** of the data.  
They help prevent invalid data from being stored — like a safety system for your database 🚦

---

## ⚖️ Types of Constraints (Rules That Keep Data in Check)

### 🧍 1. Entity Integrity Constraint
- Ensures that **each row (record)** in a table is **unique and identifiable**.  
- Usually applied through a **Primary Key**.  
- The primary key **cannot be NULL** and **must be unique**.

**Example:**

| emp_id | name   | department |
|--------:|--------|-------------|
| 1       | Alice  | HR          |
| 2       | Bob    | IT          |
| 3       | Charlie| Finance     |

✅ `emp_id` is the **Primary Key** — no duplicates, no NULLs allowed.

**SQL Example:**
`"CREATE TABLE employees ( emp_id INT PRIMARY KEY, name VARCHAR(50), department VARCHAR(50) );"`

---

### 🔗 2. Referential Integrity Constraint
- Ensures that a **Foreign Key** value always refers to an **existing record** in another table.  
- Prevents "orphan" records (e.g., an employee linked to a non-existent department).

**Example:**

**departments**

| dept_id | dept_name |
|----------|------------|
| 1        | HR         |
| 2        | IT         |

**employees**

| emp_id | name  | dept_id |
|--------:|-------|----------|
| 1       | Alice | 1        |
| 2       | Bob   | 2        |

✅ Every `dept_id` in `employees` must exist in `departments`.

**SQL Example:**
`"CREATE TABLE employees ( emp_id INT PRIMARY KEY, name VARCHAR(50), dept_id INT, FOREIGN KEY (dept_id) REFERENCES departments(dept_id) );"`

---

### 🧠 3. Semantic Integrity Constraint
- Rules that reflect **real-world meaning** of the data.  
- Ensures data makes **logical sense** according to business rules.

**Example:**  
An employee’s salary cannot be negative.  
A patient's age cannot exceed 120.

**SQL Example:**
`"ALTER TABLE employees ADD CONSTRAINT positive_salary CHECK (salary > 0);"`

---

### 🎯 4. Domain Constraint
- Defines the **valid range, type, or format** of a column’s values.  
- Ensures that each column only stores **appropriate data**.

**Example:**
`"CREATE TABLE patients ( patient_id INT PRIMARY KEY, age INT CHECK (age BETWEEN 0 AND 120), gender CHAR(1) CHECK (gender IN ('M', 'F')) );"`
✅ `age` must be between 0 and 120.  
✅ `gender` can only be ‘M’ or ‘F’.

---

### 🚫 5. Null Constraint
- Ensures that certain columns **cannot be left empty**.  
- Commonly used with **PRIMARY KEY** or **essential fields**.

**Example:**
`"CREATE TABLE devices ( device_id SERIAL PRIMARY KEY, device_name VARCHAR(100) NOT NULL, last_service_date DATE );"`
✅ `device_name` must always have a value.  
✅ `last_service_date` can be NULL (optional).

---

### ✅ 6. Check Constraint
- Used to set **specific conditions** on column values.  
- The database **checks the condition** whenever a new record is inserted or updated.

**Example:**
`"CREATE TABLE lab_results ( result_id SERIAL PRIMARY KEY, test_name VARCHAR(50), result_value DECIMAL(5,2), CHECK (result_value >= 0) );"`
✅ Ensures all test results are **non-negative**.

---

## 💡 Summary

| Constraint Type | Ensures | Example Rule |
|-----------------|----------|---------------|
| Entity Integrity | Uniqueness of rows | No duplicate primary keys |
| Referential Integrity | Valid references | Foreign key must exist in parent table |
| Semantic Integrity | Logical correctness | Salary > 0 |
| Domain Constraint | Valid data type/range | Age between 0–120 |
| Null Constraint | Required fields | Name cannot be NULL |
| Check Constraint | Custom conditions | result_value >= 0 |

---

🧩 **In short:**  
Constraints act like **rules and guardians** that keep your database reliable, consistent, and meaningful. 🚦💾



