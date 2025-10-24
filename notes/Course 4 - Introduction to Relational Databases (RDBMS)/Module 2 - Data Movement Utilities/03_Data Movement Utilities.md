# Topic: Module 2 — Creating Tables and Loading Data

---

# 🐬 MySQL – Easy & Practical Notes

## 💡 What is MySQL?
MySQL is a **relational database management system (RDBMS)** that stores and manages data using **tables**.  
It’s widely used because it’s **open-source**, **fast**, and works great for both **small** and **large-scale** applications.

---

## 🏗️ Practical Applications of MySQL

- 🌐 **Large-Scale Websites**  
  Examples: Facebook, YouTube (use MySQL variants for user data and analytics)

- 🛒 **E-Commerce Platforms**  
  Examples: Shopify, Magento — store product catalogs, user accounts, and transactions

- 🏢 **Small & Medium Businesses**  
  Examples: Local inventory systems, customer databases, POS data management

---

## 🧰 Popular MySQL Tools

### 💻 MySQL CLI (Command Line Interface)
- A text-based tool to interact directly with MySQL  
- Best for:
  - 🧑‍💻 Developers writing and testing SQL queries  
  - 🧑‍🔧 System Admins managing MySQL servers  
  - 🧮 Database Admins running maintenance tasks  

🧠 **Example:**  
To log in to MySQL:  
"mysql -u root -p"  

To view existing databases:  
"SHOW DATABASES;"

---

### ⚙️ `mysqladmin`
- Command-line utility for **administrative operations** such as:
  - Checking server status  
  - Creating or dropping databases  
  - Viewing server variables  

🧠 **Example:**  
Check MySQL server status:  
"mysqladmin -u root -p status"

---

### 🧠 MySQL Workbench
- A **desktop GUI tool** developed by Oracle  
- Useful for:
  - Designing databases visually (ER diagrams)  
  - Writing and testing SQL queries  
  - Managing users and permissions  
  - Monitoring server performance  

🧠 **Example:**  
You can design a **hospital database schema** visually and export it as SQL code for deployment.

---

### 🌍 phpMyAdmin
- A **web-based GUI** tool written in PHP  
- Commonly available on **web hosting platforms (like cPanel)**  
- Allows you to:
  - Import/export `.sql` files  
  - Browse and edit tables directly  
  - Manage databases through your browser  

🧠 **Example:**  
Manage a **WordPress** site’s posts, users, and settings without typing SQL commands.

---

## ⚖️ Comparison: MySQL Workbench vs phpMyAdmin

| 🧩 Category         | 💻 MySQL Workbench                          | 🌍 phpMyAdmin                             |
|---------------------|---------------------------------------------|-------------------------------------------|
| 🧠 Type of Tool     | Desktop Application                         | Web-Based Interface                       |
| 💰 Price            | Free (Open Source)                          | Free (Open Source)                        |
| ⚙️ Features         | ER Modeling, SQL Editor, Server Management  | Import/Export, Table Browsing, Quick Edits |
| 🧑‍💼 Target Users   | Developers, DBAs, System Admins              | Web Hosting Users, CMS Managers           |
| 💾 Example Use Case | Designing a web app database schema         | Managing a WordPress site’s database      |

---

## ✅ Summary
- 💻 **MySQL CLI** → For hands-on developers who prefer typing commands  
- ⚙️ **mysqladmin** → For quick administrative checks and maintenance  
- 🧠 **MySQL Workbench** → For database professionals managing complex data  
- 🌍 **phpMyAdmin** → For website owners managing MySQL online  

💬 **Pro Tip:**  
If you’re building or testing locally → use **MySQL Workbench**.  
If you’re managing your website online → use **phpMyAdmin**.

---

# 🏗️ Creating Databases and Tables in MySQL

Let’s explore how to create databases and tables using two tools — the **MySQL CLI** and **phpMyAdmin**.  
Both do the same thing but in very different ways 👇

---

## 💻 Using MySQL CLI (Command Line Interface)

The **CLI** is the go-to choice for developers and data engineers who like control, automation, and speed.

### 🧠 Example Steps

1. **Login to MySQL**  
   "mysql -u root -p"

2. **Create a Database**  
   "CREATE DATABASE company_db;"

3. **Use the Database**  
   "USE company_db;"

4. **Create a Table**  
   "CREATE TABLE employees (  
       emp_id INT AUTO_INCREMENT PRIMARY KEY,  
       emp_name VARCHAR(50) NOT NULL,  
       position VARCHAR(30),  
       salary DECIMAL(10,2)  
   );"

5. **View Tables**  
   "SHOW TABLES;"

6. **Describe Table Structure**  
   "DESCRIBE employees;"

✅ **Why use CLI:**  
- Faster and scriptable for automation  
- Ideal for ETL pipelines and bulk data tasks  
- Great for server-based database management  

---

## 🌍 Using phpMyAdmin

**phpMyAdmin** is a **web-based GUI tool** — perfect for beginners or web developers working on hosted sites.

### 🧠 Example Steps

1. **Login to phpMyAdmin**  
   Open your browser and go to something like:  
   "http://localhost/phpmyadmin" or "https://yourdomain.com/phpmyadmin"

2. **Create a Database**  
   - Click **“Databases”** tab  
   - Enter the database name → "company_db"  
   - Click **“Create”**

3. **Create a Table**  
   - Select "company_db"  
   - Enter table name → "employees"  
   - Number of columns → "4"  
   - Click **“Go”**

4. **Define Columns**
   - Column 1 → "emp_id", Type: "INT", Primary Key, Auto Increment  
   - Column 2 → "emp_name", Type: "VARCHAR(50)"  
   - Column 3 → "position", Type: "VARCHAR(30)"  
   - Column 4 → "salary", Type: "DECIMAL(10,2)"  
   - Click **“Save”**

✅ **Why use phpMyAdmin:**  
- Beginner-friendly with an easy graphical interface  
- Ideal for quick database setup in web projects  
- No coding required  

---

## ⚖️ Comparison: CLI vs phpMyAdmin

| 🧩 Feature          | 💻 MySQL CLI                             | 🌍 phpMyAdmin                             |
|---------------------|------------------------------------------|-------------------------------------------|
| 🔑 Access Method    | Command Line                             | Web Browser                               |
| 🧠 Skill Level      | Intermediate to Advanced                 | Beginner Friendly                         |
| ⚙️ Creating DBs     | "CREATE DATABASE company_db;"             | Click “Databases” → Enter name → Create    |
| 📋 Creating Tables  | "CREATE TABLE employees (...);"           | Use visual form to define fields           |
| 🤖 Best For         | Automation, ETL, scripting               | Web-based management, small projects       |

---

💬 **Pro Tip:**  
If you want automation or command control → use **MySQL CLI**.  
If you prefer visual database management → use **phpMyAdmin**.

---

# 📦 Populating MySQL Databases and Tables

Once your database and tables are created, the next step is to **add**, **import**, or **restore** data.  
Here’s how to do it with the most useful MySQL commands 👇

---

## 💾 Backing Up Data with `mysqldump`

### 🧠 Example:
"mysqldump -u root -p company_db > backup.sql"

### 📘 What It Means:
- **mysqldump** → the tool used to export (backup) databases  
- **-u root** → connects as the user `root`  
- **-p** → prompts you to enter your MySQL password  
- **company_db** → the name of the database you’re backing up  
- **> backup.sql** → saves the output (the SQL dump) into a file named `backup.sql`  

✅ **Result:**  
Creates a backup file containing SQL commands to recreate your entire database.

---

### 🧠 Example (specific table):
"mysqldump -u root -p company_db employees > employees_backup.sql"

### 📘 What It Means:
- This backs up **only** the `employees` table from the `company_db` database  
- The resulting file (`employees_backup.sql`) contains only that table’s structure and data  

✅ **Result:**  
You get a smaller, table-specific backup file.

---

## 🔁 Restoring Data

There are two common ways to **restore** a MySQL backup: using `mysql` or using the `SOURCE` command.

---

### 💻 1. Restore Using `mysql`
"mysql -u root -p company_db < backup.sql"

### 📘 What It Means:
- **mysql** → runs the MySQL client  
- **-u root -p** → connects as the root user (you’ll be prompted for a password)  
- **company_db** → target database to restore into  
- **< backup.sql** → redirects the SQL file into MySQL  

✅ **Result:**  
Recreates all the tables and data from the backup file inside `company_db`.

---

### 💻 2. Restore Using `SOURCE` Command
"mysql -u root -p"  
"USE company_db;"  
"SOURCE backup.sql;"

### 📘 What It Means:
- First line logs you into MySQL CLI  
- Second line tells MySQL to use the `company_db` database  
- Third line executes all SQL statements inside `backup.sql`  

✅ **Result:**  
Restores the database while you’re already inside the MySQL terminal.

---

## 📥 Loading Data into Tables

You can populate tables manually or by importing files.

---

### 🧾 Inserting Data Manually
"INSERT INTO employees (emp_name, position, salary)  
VALUES ('Alice Cruz', 'Engineer', 45000.00);"

### 📘 What It Means:
- **INSERT INTO employees (...)** → selects which table and columns to insert into  
- **VALUES (...)** → lists the actual data values in the same order as the columns  
- **('Alice Cruz', 'Engineer', 45000.00)** → adds one row to the table  

✅ **Result:**  
Adds a new record for an employee named Alice Cruz.

---

## 📂 Importing Data Files

For large datasets, it’s faster to import from `.csv` or `.txt` files.

---

### ⚙️ Importing Using `LOAD DATA INFILE`
"LOAD DATA INFILE '/path/to/employees.csv'  
INTO TABLE employees  
FIELDS TERMINATED BY ','  
LINES TERMINATED BY '\n'  
IGNORE 1 ROWS  
(emp_name, position, salary);"

### 📘 What It Means:
- **LOAD DATA INFILE '/path/to/employees.csv'** → loads data from a file into a table  
- **INTO TABLE employees** → specifies the table to insert into  
- **FIELDS TERMINATED BY ','** → says each column in the file is separated by commas  
- **LINES TERMINATED BY '\n'** → says each row ends with a new line  
- **IGNORE 1 ROWS** → skips the header row in the CSV file  
- **(emp_name, position, salary)** → matches file columns to table columns  

✅ **Result:**  
Imports all rows from `employees.csv` directly into the `employees` table.

---

### ⚙️ Importing Using `mysqlimport`
"mysqlimport -u root -p --local company_db /path/to/employees.csv"

### 📘 What It Means:
- **mysqlimport** → command-line tool for importing data files  
- **-u root -p** → connects as root and asks for a password  
- **--local** → tells MySQL to read the file from your local machine  
- **company_db** → target database  
- **/path/to/employees.csv** → the data file to import (table name should match the file name)  

✅ **Result:**  
Loads data from the CSV file into the `employees` table of the `company_db` database.

---

## ⚖️ Summary

| 🧩 Task                  | 🧠 Command or Tool Example                                | 💡 Description                                      |
|---------------------------|-----------------------------------------------------------|-----------------------------------------------------|
| 🗄️ Backup Database        | "mysqldump -u root -p company_db > backup.sql"            | Exports the database into a backup file             |
| 🧾 Backup Table           | "mysqldump -u root -p company_db employees > file.sql"    | Exports a single table                              |
| 🔁 Restore Database       | "mysql -u root -p company_db < backup.sql"                | Restores a full database from a backup              |
| 🧠 Restore via SOURCE     | "SOURCE backup.sql;"                                     | Executes a backup file from within MySQL CLI        |
| 📥 Insert Data            | "INSERT INTO employees (...) VALUES (...);"               | Adds individual records manually                    |
| ⚙️ Load Data Infile       | "LOAD DATA INFILE '/path/to/file.csv' INTO TABLE ..."     | Imports large CSV or text files into MySQL          |
| ⚙️ mysqlimport            | "mysqlimport -u root -p --local company_db file.csv"      | Imports data files directly from the command line   |

---

✅ **Final Tip:**  
- Use **`mysqldump`** → to back up databases  
- Use **`mysql`** or **`SOURCE`** → to restore backups  
- Use **`LOAD DATA INFILE`** or **`mysqlimport`** → for fast data imports  
- Use **`INSERT INTO`** → for small manual entries

---



