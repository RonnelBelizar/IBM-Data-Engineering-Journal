###############################################################
# 🧩 SQL + Python + PostgreSQL Exercise
###############################################################

# 🎯 Goal:
# Use Python to connect to PostgreSQL and practice SQL DDL/DML commands.

###############################################################
# 🧠 Instructions
###############################################################

# 1️⃣ Create a new table called 'employees' with columns:
#     - id (serial primary key)
#     - name (varchar)
#     - department (varchar)
#     - salary (numeric)

# 2️⃣ Insert at least 4 sample records into the table.

# 3️⃣ Use Python (psycopg2 + pandas) to:
#     - Connect to your PostgreSQL database
#     - Read and display the table as a DataFrame

# 4️⃣ Add a new column named 'years_of_service' with a default value of 1.
# 5️⃣ Update at least two employees' 'years_of_service' values.
# 6️⃣ Read and display the updated table again in Python.
# 7️⃣ Drop the column 'years_of_service'.
# 8️⃣ Display the final table in Python after the column is removed.
# 9️⃣ Close all database connections properly.

import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host='localhost',
    database='practice_db',
    user='postgres',
    password="Madron_91"
)

df = pd.read_sql('SELECT * FROM employees_exercise_1', conn)

print(df)

conn.close()
