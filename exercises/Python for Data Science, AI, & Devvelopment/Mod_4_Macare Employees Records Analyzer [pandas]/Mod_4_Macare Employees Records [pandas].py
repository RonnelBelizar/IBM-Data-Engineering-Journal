# ============================================================
# 👔 Exercise: Employee Records Analyzer
# ============================================================
# ✅ Focus: Pandas
# 📂 File: employees.txt
#
# Name,Age,Position,Expertise
# Ronnel,29,Engineer,Gx
# Doc,30,Engineer,Gx
# Shed,36,Engineer,Gx
# Bren,29,Engineer,Gx
# Jesh,23,Intern,None
# Rhea,25,Admin,Minutes Of Meeting
# Lara,32,It,Printer
# Harold,46,Supervisor,Management
#
# ============================================================
# ✅ Your Goals:
# ------------------------------------------------------------
# 1. Load the CSV file into a Pandas DataFrame.
# 2. Show the first 5 rows.
# 3. Count how many employees per Position.
# 4. Find the average Age per Position.
# 5. Show only employees with Age > 30.
# 6. Sort employees by Age (youngest → oldest).
# 7. BONUS:
#    - Save only Engineers into "engineers.csv".
#    - Apply .title() to Position and Expertise columns
#      in case they are not formatted properly.
# ============================================================

import pandas as pd
directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Macare Employees Records Analyzer [pandas]"
# Loading .txt as .csv
df = pd.read_csv(fr"{directory}\employees.txt")
print(df)
#      Name  Age    Position           Expertise
# 0  Ronnel   29    Engineer                  Gx
# 1     Doc   30    Engineer                  Gx
# 2    Shed   36    Engineer                  Gx
# 3    Bren   29    Engineer                  Gx
# 4    Jesh   23      Intern                 NaN
# 5    Rhea   25       Admin  Minutes Of Meeting
# 6    Lara   32          It             Printer
# 7  Harold   46  Supervisor          Management
# Showing first 5 rows
print(df.head())
# Counting employees per position
count = df.groupby("Position")["Name"].count()
print(count)
# Average age per position
ave_age = df.groupby("Position")["Age"].mean()
print(ave_age)
# Employees above 30
# in case age is not 'int'. in this exercise, age is already int
df["Age"] = df["Age"].astype(int)
above_30 = df.loc[df["Age"] > 30, ["Name", "Age"]]
print(above_30)
# Sortin by age (youngest to oldest)
age_sort = df.sort_values("Age", ascending=True)
print(age_sort)
# Saving only Engineers
engineers = df[df["Position"] == "Engineer"]
engineers.to_csv(fr"{directory}\engineers.csv", index=False)
# Apply .title() to position and expertise columns
df["Position"] = df["Position"].str.title()
df["Expertise"] = df["Expertise"].str.title()
