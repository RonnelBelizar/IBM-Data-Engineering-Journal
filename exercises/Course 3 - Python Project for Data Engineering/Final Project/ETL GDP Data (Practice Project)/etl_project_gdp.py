import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import requests
from io import StringIO
from datetime import datetime

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
header = {"User-Agent": "Mozilla/5.0"}

file = "Countries_by_GDP.csv"
table = "Countries_by_GDP"
database_file = "World_Economies.db"
attributes_db = ["Country", "GDP_USD_Billions"]
logs = "etl_project_log.txt"

sql_conn = sqlite3.connect(database_file)


def logging(message):
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(logs, "a") as log_file:
        log_file.write(f"{timestamp} INFO: {message}\n")


def extract_html():
    logging("Requesting data from URL")
    response = requests.get(url, headers=header)
    logging("Parsing html")
    soup = BeautifulSoup(response.text, "html.parser")
    html_table = str(soup.find_all("table", class_="wikitable"))
    dfs = pd.read_html(StringIO(html_table))
    df = dfs[0]
    logging("Creating DataFrame from parsed html")
    return df


def transform(extracted_data):
    to_transform_data = extracted_data.iloc[:, 0:2]
    logging("Renaming Columns")

    gdp_col = [col for col in extracted_data.columns if "IMF" in col][0]
    to_transform_data.rename(columns={
        "Country/Territory": "Country",
        gdp_col: "GDP_USD_Billions"
    }, inplace=True)

    logging("Transforming values")
    to_transform_data["GDP_USD_Billions"] = (
        to_transform_data["GDP_USD_Billions"]
        .astype(str)
        .replace({"—": 0, ",": ""}, regex=True)
        .astype(float)
        / 1000
    ).round(2)

    return to_transform_data


def saving_data(transformed_data):
    logging("Saving data (.csv)")
    transformed_data.to_csv(file, index=False)
    logging(f"Saving data as new table in {database_file}")
    transformed_data.to_sql("Countries_by_GDP",
                            sql_conn, if_exists='replace', index=False)


# RUNNING ETL
logging("Starting ETL Session...")
try:
    logging("Extracting data from the webpage...")
    extracted = extract_html()
    logging("Data successfully extracted")

    logging("Transforming extracted data...")
    transformed_data = transform(extracted)
    logging("Successfully transformed data")

    logging("Saving transformed data...")
    saving_data(transformed_data)
    logging("Successfully saved data")

    logging("ETL pipeline executed successfully")

    with open(logs, "r") as read:
        count = len(read.readlines())

    logging("\nLogging Session Finished")
    with open(logs, "a") as file:
        file.write(
            f"Total number of logs: {count}\n")
except Exception as e:
    logging(f"An error occurred during ETL execution: {e}")
finally:
    sql_conn.close()

# Testing DB Querying

with sqlite3.connect(database_file) as sql_conn:
    sql = f"SELECT * from {table} WHERE GDP_USD_Billions >= 100"
    query = pd.read_sql(sql, sql_conn)
    print(f"Countries with >= 100 GDP:  \n{query}")
