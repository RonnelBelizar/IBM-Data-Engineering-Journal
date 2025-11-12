import pandas as pd
import sqlite3

conn = sqlite3.connect("FinalDB.db")
cursor = conn.cursor()

# df = pd.read_csv("chicago_public_school.csv")
# df.to_sql("CHICAGO_PUBLIC_SCHOOL", conn, if_exists="replace", index=False)

# 1
# cursor.execute("SELECT COUNT(*) FROM chicago_crime_data;")
# count = cursor.fetchall()
# print(count)
# cursor.close()
# conn.close()

# 2
cursor.execute(
    "SELECT * FROM CENSUS_DATA WHERE PER CAPITA INCOME < 11000;")
data = cursor.fetchall()
df = pd.read_sql(data)
print(df)
cursor.close()
conn.close()
