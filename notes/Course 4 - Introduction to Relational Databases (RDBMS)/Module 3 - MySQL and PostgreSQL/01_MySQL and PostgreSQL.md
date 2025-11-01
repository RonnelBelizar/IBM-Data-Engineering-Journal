# Topic: Module 3 — MySQL and PostgreSQL

---

# 🐘 PostgreSQL Overview

PostgreSQL is a **powerful open-source relational database** known for its reliability, flexibility, and standards compliance.  
Here’s a quick and easy guide to its **deployment options** and **connectivity tools** 👇

---

## 🚀 Deployment Options

### 🖥️ 1. Local Installation
- Installed directly on your **computer or server**.  
- Great for **development, testing**, or **small projects**.  
- You have **full control** over configurations and performance.  

🧩 **Example tools:** `"PostgreSQL Installer"`, `"Homebrew (macOS)"`, `"apt/yum (Linux)"`

---

### 🧱 2. Virtualization & Containers
- PostgreSQL runs inside a **virtual machine** or a **Docker container**.  
- Makes deployment **portable and isolated** — no conflict with other systems.  
- Easier to **replicate** environments for development or production.  

🐳 **Example:** `"docker run --name my-postgres -e POSTGRES_PASSWORD=1234 -d postgres"`

---

## 🔌 Connectivity Tools

### 💻 1. psql (Command-Line Tool)
- The **official CLI** tool to connect and interact with PostgreSQL.  
- Used for running SQL queries, managing users, and databases.  

🧠 **Example:** `"psql -U postgres -d my_database"`

---

### 🧭 2. pgAdmin (Graphical Tool)
- A **GUI-based management tool**.  
- Lets you **visualize databases**, run queries, and monitor performance.  
- Great for beginners who prefer **click-based navigation** over terminal commands.  

---

### 💼 3. Commercial Options
- Offered by companies that provide **enterprise-grade PostgreSQL** with added tools, support, and performance enhancements.  
- Ideal for large organizations needing **robust backup, security, and scaling**.  

🏢 **Examples:** `"EDB Postgres"`, `"Crunchy Data"`

---

### ☁️ 4. Managed Database Services
- Fully managed PostgreSQL by **cloud providers**.  
- They handle **backups, updates, scaling**, and **maintenance**.  
- You just focus on your data and applications!  

🌐 **Examples:** `"Amazon RDS for PostgreSQL"`, `"Google Cloud SQL"`, `"Azure Database for PostgreSQL"`

---

⭐ **Summary**

| Category             | Example        | Best For            |
|----------------------|----------------|---------------------|
| 🖥️ Local             | Installed on PC | Learning, testing   |
| 🧱 Virtual/Container  | Docker, VM      | Portable setups     |
| 💻 psql              | CLI             | Developers          |
| 🧭 pgAdmin           | GUI             | Beginners           |
| 💼 Commercial        | EDB             | Enterprises         |
| ☁️ Managed           | AWS, GCP        | Cloud scalability   |

---

💡 *Tip:* Start with `"local installation"` for practice, then explore `"pgAdmin"` for management and `"Docker or cloud"` for scalable setups.

---

# 💻 Basic psql Commands (PostgreSQL CLI)

`psql` is PostgreSQL’s **command-line interface** — it lets you manage databases, run queries, and configure settings directly from your terminal.

Here’s a simple cheat sheet to get you started 👇

---

## 🚀 1. Connecting to PostgreSQL

- **Login as postgres user:**  
  `"psql -U postgres"`

- **Connect to a specific database:**  
  `"psql -U postgres -d my_database"`

- **Connect using host and port (optional):**  
  `"psql -h localhost -p 5432 -U postgres -d my_database"`

---

## 📂 2. Database Management

| Action                | Command String                    | Description                      |
|-----------------------|------------------------------------|----------------------------------|
| List all databases    | `"\\l"`                            | Shows all databases              |
| Connect to a database | `"\\c my_database"`                | Switch to another database       |
| Create a database     | `"CREATE DATABASE my_database;"`   | Creates a new database           |
| Delete a database     | `"DROP DATABASE my_database;"`     | Deletes a database               |

---

## 📦 3. Table Management

| Action                | Command String                              | Description                      |
|-----------------------|----------------------------------------------|----------------------------------|
| Show tables           | `"\\dt"`                                     | Lists all tables in current DB   |
| Create table          | `"CREATE TABLE table_name (...);"`            | Creates a new table              |
| Delete table          | `"DROP TABLE table_name;"`                   | Removes a table                  |
| Describe table        | `"\\d table_name"`                           | Displays table structure         |

---

## 🧠 4. Data Operations

| Action            | Command String                                               | Description               |
|-------------------|---------------------------------------------------------------|---------------------------|
| Insert data       | `"INSERT INTO employees VALUES (1, 'John', 'Engineer');"`     | Adds a new record         |
| View data         | `"SELECT * FROM employees;"`                                 | Displays table data       |
| Update data       | `"UPDATE employees SET name='Jane' WHERE id=1;"`             | Modifies an existing row  |
| Delete data       | `"DELETE FROM employees WHERE id=1;"`                        | Removes a record          |

---

## ⚙️ 5. User & Role Management

| Action                  | Command String                                    | Description                     |
|--------------------------|--------------------------------------------------|---------------------------------|
| List users/roles         | `"\\du"`                                         | Shows all users and roles       |
| Create new user          | `"CREATE USER ronnel WITH PASSWORD '1234';"`     | Creates a new user              |
| Grant privileges         | `"GRANT ALL PRIVILEGES ON DATABASE my_db TO ronnel;"` | Gives permissions to user |
| Change user password     | `"ALTER USER ronnel WITH PASSWORD 'newpass';"`   | Updates password                |

---

## 🧩 6. Meta Commands (Starts with `\`)

| Command String | Description                              |
|----------------|------------------------------------------|
| `"\\?"`        | Lists all available psql commands        |
| `"\\q"`        | Quits the psql shell                     |
| `"\\dt"`       | Lists tables                            |
| `"\\d"`        | Describes a table or view structure      |
| `"\\du"`       | Lists users and roles                    |
| `"\\l"`        | Lists all databases                      |
| `"\\c"`        | Connects to a database                   |

---

## 💾 7. Import / Export Data

| Action             | Command String                                      | Description                    |
|--------------------|------------------------------------------------------|--------------------------------|
| Import SQL file    | `"\\i path/to/script.sql"`                           | Runs SQL file into database    |
| Export query result| `"\\o output.txt"` then run a query                  | Saves query output to file     |
| Stop export        | `"\\o"`                                              | Returns output to screen       |

---

## 🧠 Quick Summary

| Task                | Command Example                |
|----------------------|--------------------------------|
| Login to psql        | `"psql -U postgres"`           |
| List databases       | `"\\l"`                        |
| Create database      | `"CREATE DATABASE test_db;"`   |
| Switch database      | `"\\c test_db"`                |
| Show tables          | `"\\dt"`                       |
| Quit psql            | `"\\q"`                        |

---

💡 **Pro Tip:**  
You can type `"\\? "` anytime in `psql` to see a full list of commands.  
It’s like your built-in help guide! 🚀

---

# 👁️ PostgreSQL Views Overview

In PostgreSQL, **Views** are like **virtual tables** — they don’t store data themselves but show data from one or more tables based on a saved query.  
They help simplify complex SQL and improve data security by limiting what users can see.  

Let’s break it down 👇

---

## 🔹 1. View (Regular View)

### 🧠 What It Is:
A **view** is a **saved SQL query** that acts like a table.  
When you query it, PostgreSQL runs the underlying query in real time.

### 🏗️ How It Works:
- It **does not store data** — it pulls fresh data from the source tables every time.
- Used for **simplifying queries** and **restricting access** to sensitive columns.

### 🧩 Create a View:
`"CREATE VIEW view_name AS SELECT columns FROM table_name WHERE condition;"`

📘 **Example:**
`"CREATE VIEW active_patients AS SELECT patient_id, first_name, last_name FROM patients WHERE status = 'Active';"`

Now you can query it like a normal table:
`"SELECT * FROM active_patients;"`

### 🔄 Update a View:
`"CREATE OR REPLACE VIEW view_name AS SELECT ...;"`

### ❌ Delete a View:
`"DROP VIEW view_name;"`

---

## 🔸 2. Materialized View

### 🧠 What It Is:
A **materialized view** is like a view, **but it stores the query result** physically on disk.  
This makes it **faster to query**, especially for large or complex data — but the data can get **outdated**.

### 🏗️ How It Works:
- It **stores data** like a snapshot.
- You need to **manually refresh** it to update the data.

### 🧩 Create a Materialized View:
`"CREATE MATERIALIZED VIEW sales_summary AS SELECT region, SUM(amount) AS total_sales FROM sales GROUP BY region;"`

### 🔄 Refresh Data:
`"REFRESH MATERIALIZED VIEW sales_summary;"`

### ❌ Delete a Materialized View:
`"DROP MATERIALIZED VIEW sales_summary;"`

---

## ⚖️ 3. Key Differences

| Feature                 | View                     | Materialized View              |
|--------------------------|--------------------------|--------------------------------|
| 📦 Data Storage          | Does **not** store data  | **Stores** query results       |
| ⚡ Performance           | Slower (runs query each time) | Faster (reads from stored data) |
| 🔄 Data Freshness        | Always up-to-date        | Needs manual refresh           |
| 🧰 Use Case              | Dynamic, live data        | Pre-computed or large datasets |
| 🔁 Refresh Command       | Not needed               | `"REFRESH MATERIALIZED VIEW"`  |

---

💡 **Tip:**  
Use a **regular view** for data that changes frequently.  
Use a **materialized view** when performance is more important than real-time accuracy.

