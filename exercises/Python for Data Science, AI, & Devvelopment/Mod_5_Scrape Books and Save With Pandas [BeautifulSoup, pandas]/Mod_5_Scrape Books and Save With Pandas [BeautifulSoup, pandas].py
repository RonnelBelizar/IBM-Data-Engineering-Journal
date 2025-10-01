# 🕸️ + 🐼 Exercise: Scrape Books & Save with Pandas
# ================================================================
# Goal:
# 1. Fetch the page HTML from http://books.toscrape.com
# 2. Extract for each book:
#    - Title
#    - Price
#    - Availability
# 3. Store the data in a Pandas DataFrame
# 4. Save the DataFrame to a CSV file
# 5. Print the first 5 rows

import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com"
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

main_container = soup.find_all("article", class_="product_pod")
titles = []
prices = []
availability = []

for data in main_container:
    book_title = data.h3.a["title"]
    titles.append(book_title)

    book_price = data.find("p", class_="price_color").get_text()
    prices.append(book_price)

    avail = data.find("p", class_="instock availability").get_text().strip()
    availability.append(avail)

records = {"Book": titles,
           "Price": prices,
           "Availability": availability}

df = pd.DataFrame(records)

directory = r'C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_5_Scrape Books and Save With Pandas [BeautifulSoup, pandas]'
df.to_csv(fr"{directory}\inventory.csv", index=False)

print(df.head())
