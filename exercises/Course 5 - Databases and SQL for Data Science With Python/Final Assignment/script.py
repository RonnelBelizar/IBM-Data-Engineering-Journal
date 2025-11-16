import pandas as pd
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine("mysql+pymysql://Ronnel:1234@localhost/finaldb")

# Loading Census Data

df_census = pd.read_csv("ChicagoCensusData.csv")
df_census.columns = df_census.columns.str.strip().str.replace(' ', '_').str.lower()
df_census.to_sql("CENSUS_DATA", engine, if_exists="replace", index=False)

# Loading Chicago Crime Data

df_crime = pd.read_csv("ChicagoCrimeData.csv")
df_crime.columns = df_crime.columns.str.strip().str.replace(' ', '_').str.lower()
df_crime.to_sql("CHICAGO_CRIME_DATA", engine, if_exists="replace", index=False)

# Loading Chicago Public School

df_school = pd.read_csv("ChicagoPublicSchools.csv")
df_school.columns = df_school.columns.str.strip().str.replace(' ', '_').str.lower()
df_school.to_sql("CHICAGO_PUBLIC_SCHOOLS", engine,
                 if_exists="replace", index=False)

engine.dispose()
