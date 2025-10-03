# ============================================================
# ✅ Goal: Pull data from the SpaceX public API, process it, and analyze launches.
#
# 📌 Instructions:
# 1. Install requirements:
#       pip install requests pandas
# 2. Use the API endpoint:
#       https://api.spacexdata.com/v4/launches
# 3. Tasks:
#    1️⃣ Call the API and load the data.
#    2️⃣ Convert the JSON into a pandas DataFrame.
#    3️⃣ Display the first 10 launches with columns:
#       - name (mission name)
#       - date_utc (launch date)
#       - success (True/False)
#       - rocket (rocket ID)
#    4️⃣ Count how many launches were successful vs failed.
#    5️⃣ (Challenge 🚀) Find the latest launch and print its mission name & date.
# ============================================================

import pandas as pd
import requests

url = "https://api.spacexdata.com/v4/launches"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

new_df = df[["name", "date_utc", "success", "rocket"]]

success = new_df[new_df["success"] == True]

print(success["success"].count())

new_df["date_utc"] = pd.to_datetime(new_df["date_utc"])

sort = new_df.sort_values("date_utc", ascending=False)

print(sort.head())
print("Latest Launch")
print(f"Mission Name: {sort.iloc[0, 0]} \nLaunch Date: {sort.iloc[0, 1]}")