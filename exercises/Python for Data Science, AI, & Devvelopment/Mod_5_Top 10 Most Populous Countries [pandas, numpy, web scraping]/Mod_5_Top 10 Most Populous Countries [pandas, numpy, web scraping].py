# 🌍 Practice Project: Top 10 Most Populous Countries
#
# 📌 Scenario
# You are a junior Data Engineer at a logistics company.
# Your manager wants the list of the top 10 most populous countries in the world,
# sorted in descending order by population, extracted directly from Wikipedia.
#
# 🎯 Objectives
# - Use Webscraping to extract information from a website.
# - Use Pandas to load and process tabular data as a DataFrame.
# - Use NumPy to manipulate the DataFrame.
# - Export the results to a CSV file.
#
# 🔗 Data Source
# Wikipedia: List of countries by population (United Nations)
# https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)
#
# 📝 Instructions
# 1. Use Pandas to scrape the table from the provided Wikipedia link.
# 2. Identify and select the table containing the population data.
# 3. Clean the data by keeping only the Country and Population columns.
# 4. Convert the population numbers into integers (removing commas if needed).
# 5. Sort the countries by population in descending order.
# 6. Extract the top 10 most populous countries.
# 7. Save the final results to a CSV file named `top10_populous_countries.csv`.

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
header = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, "html.parser")
tables = soup.find_all("table")

table = pd.read_html(StringIO(str(tables[0])))
df = table[0]

df_clean = df[["Country or territory",
               "Population (1 July 2022)", "Population (1 July 2023)"]].copy()

df_clean["Population (1 July 2022)"] = df_clean["Population (1 July 2022)"].astype(
    int)

df_sort = df_clean.sort_values(
    "Population (1 July 2023)", ascending=False).reset_index(drop=True)

df_new = df_sort.drop(0).reset_index(drop=True)

print(df_new)

directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_5_Top 10 Most Populous Countries [pandas, numpy, web scraping]"
df_new.iloc[0:9].to_csv(
    fr"{directory}\top10_populous_countries.csv", index=False)
