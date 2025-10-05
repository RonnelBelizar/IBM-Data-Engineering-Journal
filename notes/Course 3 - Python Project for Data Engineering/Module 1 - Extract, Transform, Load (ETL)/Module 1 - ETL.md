# Topic: Module 1 - ETL

# 🛠️ Data Engineering Notes: ETL Basics

## ETL (Extract, Transform, Load)
The process of **extracting** data from sources, **transforming** it into a usable format, and **loading** it into a target system (database, data warehouse, etc.).  

### Basic ETL Components

**1. `glob` function**  
- Used to **retrieve files** from a directory matching a pattern (e.g., all `.csv` files).  
- Example:
    ```python
    import glob
    files = glob.glob("/data/*.csv")
    ```

**2. `datestamp` function**  
- Adds a **timestamp** to files or logs to track processing times or versions.  
- Example:
    ```python
    from datetime import datetime
    datestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{datestamp}.csv"
    ```

**3. `logging` function**  
- Tracks **ETL process events**, errors, or important milestones.  
- Example:
    ```python
    import logging
    logging.basicConfig(level=logging.INFO, filename='etl.log')
    logging.info("ETL process started")
    logging.error("Error loading file")
    ```

### Simple Example: Basic ETL Pipeline
```python
import glob
import pandas as pd
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, filename='etl.log')
logging.info("ETL process started")

# Extract: get all CSV files
files = glob.glob("data/*.csv")
all_data = []

for file in files:
    logging.info(f"Processing {file}")
    df = pd.read_csv(file)
    
    # Transform: simple example - add datestamp column
    df['datestamp'] = datetime.now().strftime("%Y-%m-%d")
    all_data.append(df)

# Load: combine all data and save to output CSV
final_df = pd.concat(all_data, ignore_index=True)
output_file = f"output_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
final_df.to_csv(output_file, index=False)
logging.info(f"ETL process finished, saved to {output_file}")
```

---

# 🧩 SQLite3 in Python — Your Pocket Database

SQLite3 is an **in-process Python library** that implements a **self-contained**, **serverless**, **zero-configuration**, and **transactional SQL database engine**.  
It’s widely used for **local or embedded storage** — perfect for applications that don’t need a full database server. 💡  

> ✅ Fun fact: SQLite3 comes *pre-installed* with Python! No need for extra installs — it’s ready to go out of the box.

---

## ⚙️ 1. Connecting to an SQLite3 Database

```python
import sqlite3

# 🔗 Create or connect to a database
sql_connection = sqlite3.connect('database.db')
```

🧠 **Note:**  
- If `'database.db'` doesn’t exist, SQLite will automatically create it in your working directory.  
- The connection object acts like a “gateway” between Python and your database.

---

## 🧱 2. Creating a Table using Pandas + SQLite3

```python
df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
```

### 📝 Parameters explained:
- **`table_name`** → name of the table you want to create.  
- **`sql_connection`** → your active SQLite3 connection.  
- **`if_exists`** → what to do if the table already exists:
  - `'fail'` ❌ → do nothing, raise an error.
  - `'replace'` 🔁 → overwrite the existing table.
  - `'append'` ➕ → add new data to the existing table.
- **`index`** → set to `True` only if the DataFrame index contains useful info.

💡 **Pro Tip:**  
SQLite3 is great for small projects or prototypes, but not ideal for highly concurrent apps — it locks the database during writes.

---

## 🔍 3. Querying the Database with Pandas

```python
import pandas as pd

# 🧾 Execute a SQL query and store the result in a DataFrame
df = pd.read_sql(query_statement, sql_connection)
```

🧠 **Tip:**  
The `query_statement` argument should be a valid SQL query string — for example:  
```python
query_statement = "SELECT * FROM employees WHERE salary > 50000"
```

---

## 📊 4. Example SQL Queries You Should Know

```
+----------------------------------------------+-------------------------------------------------------------+
| 💬 Query Statement                           | 🧠 Purpose                                                   |
+----------------------------------------------+-------------------------------------------------------------+
| SELECT * FROM table_name                     | Retrieve all rows and columns.                              |
| SELECT COUNT(*) FROM table_name              | Count total number of entries.                              |
| SELECT column_name FROM table_name           | Get values from a specific column.                          |
| SELECT * FROM table_name WHERE condition     | Filter data using a condition (e.g. age > 30).              |
+----------------------------------------------+-------------------------------------------------------------+
```

---

## 💾 Extra Nuggets of Knowledge

- SQLite3 stores data in a **single `.db` file**, making it portable and easy to back up.  
- You can explore your database visually using tools like **DB Browser for SQLite** or **SQLiteStudio**.  
- Always **close your connection** after use to prevent file locks:  
  ```python
  sql_connection.close()
  ```

---

## 🧠 Summary

```
+-----------------------------------------+------------------------------------------------------------+
| 🔧 Task                                 | 💡 Command                                                 |
+-----------------------------------------+------------------------------------------------------------+
| Create DB connection                    | sqlite3.connect('database.db')                             |
| Write DataFrame to table                | df.to_sql(table_name, sql_connection)                      |
| Query table into DataFrame              | pd.read_sql(query, sql_connection)                         |
| Close connection                        | sql_connection.close()                                     |
+-----------------------------------------+------------------------------------------------------------+
```

---

> 💬 **In short:** SQLite3 is your lightweight, built-in database buddy — perfect for practice, prototypes, and local data analysis. 🚀


