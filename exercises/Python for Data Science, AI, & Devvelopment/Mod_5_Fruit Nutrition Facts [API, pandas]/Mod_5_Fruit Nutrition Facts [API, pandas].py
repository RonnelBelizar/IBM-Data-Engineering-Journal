# 🍎 Exercise: Fruit Nutrition Facts
# ============================================================
# ✅ Focus: API + Pandas
#
# 📌 API: Fruityvice API → https://www.fruityvice.com/api/fruit/all
# ------------------------------------------------------------
# 📝 Task:
# 1. Call the API and get the fruit data.
# 2. Convert the JSON into a Pandas DataFrame.
#    - Keep columns: name, family, genus, carbohydrates, protein, fat, calories, sugar
# 3. Show the first 5 fruits.
# 4. Find the fruit with the highest sugar content.
# 5. Filter all fruits with calories < 50.
# 6. BONUS 🚀: Save the DataFrame into fruits.csv
# ============================================================

import requests
import pandas as pd

# Calling fruit data from API
url = r"https://www.fruityvice.com/api/fruit/all"
response = requests.get(url)
data = response.json()

# Converting JSON into DataFrame
df = pd.json_normalize(data)
new_df = df[["name", "family", "genus", "nutritions.carbohydrates",
             "nutritions.protein", "nutritions.fat", "nutritions.calories", "nutritions.sugar"]]

# Showing first 5 fruits
print((new_df.head()))

# Finding fruit with highest sugar content
highest_sugar = new_df.sort_values(
    "nutritions.sugar", ascending=False).reset_index()
print(highest_sugar)
print(
    f'{highest_sugar.loc[0, "name"]}: {highest_sugar.loc[0, "nutritions.sugar"]}')

# Filtering fruits with calories < 50
calories_50 = new_df[new_df["nutritions.calories"] < 50].sort_values(
    "nutritions.calories", ascending=False).reset_index(drop=True)
print(calories_50)

# Saving DataFrame
directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_5_Fruit Nutrition Facts [API, pandas]"
new_df.to_csv(fr"{directory}\fruits.csv", index=False)
