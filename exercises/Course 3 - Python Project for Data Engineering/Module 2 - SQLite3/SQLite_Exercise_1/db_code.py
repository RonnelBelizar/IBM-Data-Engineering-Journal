# 🧠 SQLite3 Exercise: PATIENTS Database
# ======================================

# 1️⃣ Create or connect to a database named HOSPITAL.db
# 2️⃣ Define table name as 'PATIENTS' and attributes:
#    PATIENT_ID, FIRST_NAME, LAST_NAME, AGE, DIAGNOSIS, CITY
# 3️⃣ Load data from 'PATIENTS.csv' using the attribute list as column names
# 4️⃣ Create the SQL table and store the CSV data inside it

# 5️⃣ Query 1: Display all patient records
# 6️⃣ Query 2: Show only patients older than 50
# 7️⃣ Query 3: Count how many patients are from each city

# 8️⃣ Append one new patient record (use any data you want)

# 9️⃣ Query 4: Display the total number of patients after appending

# 🔚 Close the database connection

import sqlite3
import pandas as pd

# Creating db connection
sql_conn = sqlite3.connect("HOSPITAL.db")

table_name = "PATIENTS"
columns = ['PATIENT_ID', 'FIRST_NAME', 'LAST_NAME', 'AGE', 'DIAGNOSIS', 'CITY']

# Extracting CSV
df = pd.read_csv("PATIENTS.csv", names=columns)

# Creating a Table on db
df.to_sql(table_name, sql_conn, if_exists='replace', index=False)

# Querying
sql_display_all = f"SELECT * FROM {table_name}"
sql_query_1 = pd.read_sql(sql_display_all, sql_conn)
print(sql_query_1)

sql_show_above50 = f"SELECT * FROM {table_name} WHERE AGE > 50"
sql_query_2 = pd.read_sql(sql_show_above50, sql_conn)
print(sql_query_2)

sql_pt_city = f"SELECT CITY, COUNT(*) AS Patient_Count FROM {table_name} GROUP BY CITY"
sql_query_3 = pd.read_sql(sql_pt_city, sql_conn)
print(sql_query_3)

# Adding new patient
new_patient = {'PATIENT_ID': [1002], 'FIRST_NAME': ["John"], 'LAST_NAME': [
    "Doctor"], 'AGE': [30], 'DIAGNOSIS': ["HIV"], 'CITY': ["Cainta"]}

new_df = pd.DataFrame(new_patient)

new_df.to_sql(table_name, sql_conn, if_exists='append', index=False)

# Final query

sql_final = f"SELECT COUNT (*) AS PATIENT_COUNT FROM {table_name}"
sql1 = pd.read_sql(sql_final, sql_conn)
sql_final_2 = f"SELECT * FROM {table_name}"
sql_2 = pd.read_sql(sql_final_2, sql_conn)

print(f"{sql1} \n{sql_2}")

# Closing db
sql_conn.close()
