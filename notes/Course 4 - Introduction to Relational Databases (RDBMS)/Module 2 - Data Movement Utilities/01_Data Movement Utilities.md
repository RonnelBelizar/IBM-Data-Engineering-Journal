# Topic: Module 2 — Creating Tables and Loading Data

---

# 🧩 Types of SQL Statements

SQL statements are divided into groups based on what they do — some define the structure of the database, while others handle the data inside it.

---

## 🏗️ DDL (Data Definition Language)
**Purpose:** Defines and manages database structures such as tables and schemas.  
Think of it as **"designing the blueprint"** of the database.

**Examples:**
- `CREATE TABLE employees (id INT, name VARCHAR(50));` → creates a table  
- `ALTER TABLE employees ADD COLUMN salary DECIMAL(10,2);` → changes structure  
- `DROP TABLE employees;` → removes the table  

🧠 **Tip to Remember:** DDL = *Define, Design, Layout*

---

## ✏️ DML (Data Manipulation Language)
**Purpose:** Works with the data stored inside tables.  
Think of it as **"filling in and updating the records"** of your database.

**Examples:**
- `INSERT INTO employees (id, name, salary) VALUES (1, 'Alice', 50000);` → add data  
- `SELECT * FROM employees;` → read data  
- `UPDATE employees SET salary = 55000 WHERE id = 1;` → modify data  
- `DELETE FROM employees WHERE id = 1;` → remove data  

🧠 **Tip to Remember:** DML = *CRUD (Create, Read, Update, Delete)*

---

## 📝 Summary

| Category | Meaning                    | Main Use                        | Easy Way to Remember   |
|-----------|----------------------------|----------------------------------|------------------------|
| **DDL**   | Data Definition Language   | Defines database structure       | “Design the layout”    |
| **DML**   | Data Manipulation Language | Works with the data in tables    | “Manage the data”      |

💡 **Quick Trick:**  
➡️ DDL builds the house 🏠  
➡️ DML lives in it 🧍‍♂️

---

# 🏗️ Creating Tables in SQL

Creating tables is a fundamental part of designing a database. A table defines how data will be stored, organized, and related to other data.

---

## Key Considerations
Before creating a table, you need to plan its structure and where it belongs.

- **Consider Schemas** – A schema is a logical container that holds tables, views, and other database objects.  
  It helps organize data and control access.  

  **Example:**  
  - `sales.employees` → table inside the *sales* schema  
  - `hr.staff` → table inside the *hr* schema  

  💡 **Think of a schema as a folder** that keeps related tables together.

- **Collect Information** – Identify the kind of data the table will store, such as employee details, product lists, or patient records.  
  Example: Decide which columns you need (e.g., ID, Name, Salary, Date).

---

## Methods for Creating Tables
There are several ways to create tables depending on your tools:

- **Visual Interface or UI** – Tools like MySQL Workbench or pgAdmin allow you to design tables using a graphical form without typing SQL.  
- **Using SQL Statements** – The most direct way is through the `CREATE TABLE` command.  
  **Example:**  
  `CREATE TABLE sales.employees (id INT PRIMARY KEY, name VARCHAR(50), salary DECIMAL(10,2));`  
- **Using APIs** – Some software applications or ORMs (like SQLAlchemy or Django ORM) can create tables automatically through code.

---

## Table Creation Steps
1. **Selecting a Schema** – Choose the schema where your table will be created.  
   Example: `CREATE TABLE hr.employees (...);`  
2. **Creating the Table** – Use SQL or a database tool to define your table.  
   Example: `CREATE TABLE employees (id INT, name VARCHAR(50));`  
3. **Configuring Columns** – Set column names, data types, and constraints (e.g., `PRIMARY KEY`, `NOT NULL`).  
   Example: `salary DECIMAL(10,2) NOT NULL`  
4. **Post Creation** – Add relationships, indexes, or permissions after the table is created.  
   Example: `CREATE INDEX idx_salary ON employees(salary);`

---

## Summary

| Step | Description                 | Example / Tip                                        |
|------|-----------------------------|------------------------------------------------------|
| 1️⃣  | **Select Schema**           | `CREATE TABLE sales.products (...);`                 |
| 2️⃣  | **Create Table**            | Use `CREATE TABLE` or a visual UI                    |
| 3️⃣  | **Configure Columns**       | Add names, data types, and constraints               |
| 4️⃣  | **Post Creation**           | Add indexes, relationships, or permissions           |

💡 **Easy Reminder:** **S-C-C-P → Schema → Create → Configure → Post**

---

# 🧱 CREATE TABLE Statement

The CREATE TABLE statement is used to define and create a new table in a database. It specifies the table name, columns, and their data types.

## Syntax
CREATE TABLE table_name (
    column1 data_type constraint,
    column2 data_type constraint,
    ...
);

## Example
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

This creates a table named employees with columns for id, name, position, salary, and hire_date.

## Common Constraints
Constraints are rules that help maintain data integrity.

| Constraint       | Description                                              | Example Usage                                     |
|------------------|----------------------------------------------------------|--------------------------------------------------|
| PRIMARY KEY      | Uniquely identifies each record in the table             | id INT PRIMARY KEY                               |
| NOT NULL         | Ensures the column cannot have a NULL value              | name VARCHAR(50) NOT NULL                        |
| UNIQUE           | Ensures all values in a column are different             | email VARCHAR(100) UNIQUE                        |
| DEFAULT          | Assigns a default value when no data is provided         | status VARCHAR(10) DEFAULT 'Active'              |
| CHECK            | Ensures values meet a specific condition                 | salary DECIMAL(10,2) CHECK (salary > 0)          |
| FOREIGN KEY      | Creates a link between two tables                        | FOREIGN KEY (dept_id) REFERENCES departments(id)  |

## Example with Schema
CREATE TABLE hr.employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    dept_id INT,
    salary DECIMAL(10,2) CHECK (salary > 0),
    FOREIGN KEY (dept_id) REFERENCES hr.departments(dept_id)
);

This example:
- Belongs to the hr schema
- Has a foreign key linking employees to departments
- Ensures salary values are positive

## Summary
| Keyword / Concept | Meaning / Purpose                                   | Example / Tip                                      |
|--------------------|----------------------------------------------------|----------------------------------------------------|
| CREATE TABLE       | Defines and creates a new table                    | CREATE TABLE employees (...);                      |
| Column             | Defines data fields of the table                   | name VARCHAR(50)                                   |
| Constraint         | Adds rules for data accuracy and consistency       | PRIMARY KEY, NOT NULL, CHECK                       |
| Schema             | Logical container for tables and other objects     | hr.employees                                       |
| Best Practice      | Always specify constraints to ensure data quality  | salary DECIMAL(10,2) CHECK (salary > 0)            |

💡 Quick Tip: CREATE TABLE defines the structure — not the data itself.

---

# ⚙️ ALTER, DROP, and TRUNCATE Statements

These SQL commands are part of **DDL (Data Definition Language)**. They are used to modify, remove, or reset database tables and their structures.

---

## 🔹 ALTER
The `ALTER` statement is used to **change the structure of an existing table**.  
You can add, modify, or delete columns, and also rename the table.

**Examples:**
- Add a new column:  
  `ALTER TABLE employees ADD COLUMN department VARCHAR(50);`
- Modify a column:  
  `ALTER TABLE employees MODIFY COLUMN salary DECIMAL(12,2);`
- Drop a column:  
  `ALTER TABLE employees DROP COLUMN position;`
- Rename a table:  
  `ALTER TABLE employees RENAME TO staff;`

🧠 **Use when:** You need to update the design of an existing table without recreating it.

---

## 🔹 DROP
The `DROP` statement is used to **delete an entire table or database permanently**.  
Once dropped, all data and structure are lost.

**Examples:**
- Drop a table:  
  `DROP TABLE employees;`
- Drop a database:  
  `DROP DATABASE company;`

⚠️ **Warning:** Use with caution — it **cannot be undone**.

🧠 **Use when:** You no longer need the table or database.

---

## 🔹 TRUNCATE
The `TRUNCATE` statement is used to **remove all records from a table** but **keep its structure**.  
Unlike `DELETE`, it cannot have a `WHERE` clause and is faster for clearing large tables.

**Examples:**
- Remove all data:  
  `TRUNCATE TABLE employees;`

🧠 **Use when:** You want to quickly clear all data while keeping the table ready for reuse.

---

## 🧠 Summary

| Command  | Purpose                                  | Keeps Table Structure | Can Be Undone | Example                                |
|-----------|------------------------------------------|-----------------------|----------------|----------------------------------------|
| **ALTER** | Modify table structure                   | ✅ Yes                | ✅ Usually     | `ALTER TABLE employees ADD age INT;`   |
| **DROP**  | Delete table or database permanently     | ❌ No                 | ❌ No          | `DROP TABLE employees;`                |
| **TRUNCATE** | Remove all rows but keep structure    | ✅ Yes                | ❌ No          | `TRUNCATE TABLE employees;`            |

💡 **Quick Tip:**  
**ALTER** changes the table, **DROP** destroys it, and **TRUNCATE** cleans it.

---

# 🧱 Data Movement Utilities

Data movement utilities are tools that help you **transfer, copy, or back up data** between databases or external files. They are essential for **migration, backup, sharing, and ETL (Extract, Transform, Load)** processes.

Scenarios for Data Movement:
- Database Migration – moving data from one database to another (for example, from testing to production)
- Backup and Recovery – keeping safe copies of data in case of loss or damage
- Data Import and Export – sharing or receiving data between systems
- ETL (Extract, Transform, Load) – extracting data, modifying it, and loading it into another database

Data Movement Tools and Utilities:
1. Backup and Restore – used to save the entire database and recover it later if needed  
   Example:  
   pg_dump mydb > backup.sql  
   psql mydb < backup.sql  
   Think of this like copying a folder so you can restore it later.  

2. Import and Export – used to move table data in and out of the database  
   Example (PostgreSQL):  
   COPY employees TO 'C:\exports\employees.csv' DELIMITER ',' CSV HEADER;  
   COPY employees FROM 'C:\imports\employees.csv' DELIMITER ',' CSV HEADER;  
   Think of this like saving an Excel sheet from your database or uploading one back into it.  

Common Data Formats:

| Format   | Description                                                        | Common Use                            |
|-----------|--------------------------------------------------------------------|---------------------------------------|
| DEL       | Delimited text using commas, tabs, or pipes as separators          | CSV or text file exports              |
| ASC       | Plain ASCII text, human-readable                                   | Simple backups                        |
| PC/IXF    | Platform-independent format containing both structure and data     | Moving data across different systems  |
| JSON      | JavaScript Object Notation; structured key-value data              | APIs and modern web data exchange     |

Example JSON data:  
{id: 101, name: "Ronnel Belizar", department: "Engineering"}

Summary Table:

| Tool / Utility | What It Does                          | Example Command / Use                 |
|-----------------|---------------------------------------|--------------------------------------|
| Backup          | Saves the entire database for recovery| pg_dump mydb > backup.sql            |
| Restore         | Loads a saved database backup         | psql mydb < backup.sql               |
| Import          | Loads data from an external file      | COPY employees FROM 'file.csv' CSV;  |
| Export          | Saves table data to an external file  | COPY employees TO 'file.csv' CSV;    |

Tip to Remember:  
“BIRE” – Backup, Import, Restore, Export — the 4 key data movement operations.

---





