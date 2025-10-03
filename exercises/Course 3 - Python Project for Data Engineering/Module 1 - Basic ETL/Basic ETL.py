import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import glob
url = r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip"

for_output = "transformed_data.csv"
log_file = "log_file.txt"


def extract_csv(file_csv):
    df = pd.read_csv(file_csv)
    return df


def extract_json(file_json):
    df = pd.read_json(file_json, lines=True)
    return df


def extract_xml(file_xml):
    df = pd.DataFrame(
        columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_xml)
    root = tree.getroot()

    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        df = pd.concat([df, pd.DataFrame(
            [{"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel}])], ignore_index=True)

    return df


def extract():
    extracted_data = pd.DataFrame(
        columns=["car_model", "year_of_manufacture", "price", "fuel"])

    for csv in glob.glob("*.csv"):
        if csv != for_output:
            extracted_data = pd.concat(
                [extracted_data, pd.DataFrame(extract_csv(csv))], ignore_index=True)

    for json in glob.glob("*.json"):
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_json(json))], ignore_index=True)

    for xml in glob.glob("*.xml"):
        extracted_data = pd.concat(
            [extracted_data, pd.DataFrame(extract_xml(xml))], ignore_index=True)

    return extracted_data


def transform(data):
    data["price"] = data["price"].round(2).copy()
    return data


def load(file):
    file.to_csv(for_output, index=False)


def log(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open(log_file, "a") as f:
        f.write(timestamp + ',' + message + '\n')

# ---------------------------------


log("ETL Started")
log("Extraction in Progress")
extracted_data = extract()
log("Extraction Ended")
log("Transformation Started")
transformed_data = transform(extracted_data)
log("Transformation Ended")
log("Saving Transformed Data")
load(transformed_data)
log("Saving Successful")
