import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import datetime
from io import StringIO


url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
header = {"User-Agent": "Mozilla/5.0"}

attributes = ["Name", "MC_USD_Billion"]
table_attributes = ["Name", "MC_USD_Billion",
                    "MC_GBP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]

output_csv_path = "Largest_banks_data.csv"
database_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"


def log_progress(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as logging:
        logging.write(f"{timestamp_format}: {message}")


def extract(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = str(soup.find_all("table", class_="wikitable"))
    dfs = pd.read_html(StringIO(tables))
    df = dfs[0]
    return df


def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    return df


extracted = extract(url)
exchange_rate = pd.read_csv("exchange_rate.csv")

final_table_format = pd.DataFrame(columns=table_attributes)
new = extracted.rename(columns={
    "Bank name": "Name", "Total assets (2025) (US$ billion)": "MC_USD_Billion"})
df = pd.concat([final_table_format, new], ignore_index=True)

df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'], 2)
                        for x in df['MC_GBP_Billion']]
df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'], 2)
                        for x in df['MC_EUR_Billion']]
df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'], 2)
                        for x in df['MC_INR_Billion']]

print(df)
