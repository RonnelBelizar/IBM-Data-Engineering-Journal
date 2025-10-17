###############################################################
# 🧩 Real-World Python + SQL Exercise: Employee Salary & Bonus
###############################################################

# 🎯 Goal: Practice Python + PostgreSQL by managing employee salaries and bonus eligibility.

###############################################################
# 🧠 Instructions
###############################################################

# 1. Connect to your PostgreSQL database using Python (psycopg2).
# 2. Read the existing table `employees_exercise_1` into a pandas DataFrame and display all employee records.
# 3. Give a 10% salary increase to all employees in the `Engineering` department.
# 4. Add a new column `bonus_eligible` to the table with default value FALSE.
# 5. Update the `bonus_eligible` column: set it to TRUE for employees with salary > 50000.
# 6. Read and display the updated table again in Python to verify your changes.
# 7. Close all database connections properly.

# 💡 Notes:
# - Use SQL commands (SELECT, UPDATE, ALTER TABLE) within Python.
# - Commit your changes to make sure updates are saved.
# - Use pandas to easily view the table after each modification.
# - Keep track of the order: first select → then update → then alter → then verify.

import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='practice_db',
    user='postgres',
    password='Madron_91'
)

df = pd.read_sql('SELECT * FROM employees_exercise_1', conn)
print(df)
conn.close()
