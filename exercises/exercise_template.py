import requests
import mysql.connector
import pandas as pd

url_crimes = "https://data.cityofchicago.org/api/v3/views/ijzp-q8t2/query.json"
header = {"User-Agent": "Mozilla/5.0"}


# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="mydatabase"
# )

response = requests.get(url_crimes, headers=header)
data = response.json()

rows = data["data"]
columns = [col["name"] for col in data["meta"]["view"]["columns"]]

df = pd.DataFrame(rows, columns=columns)

print(df.head())
